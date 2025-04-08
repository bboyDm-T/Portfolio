import os
# import time
import zipfile
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import io
from multiprocessing import Pool, cpu_count
import threading

# Output directory for CSVs
output_dir = "csv_output"
os.makedirs(output_dir, exist_ok=True)

# ATC codes to scrape (large database, if you select all, uncomment with caution)
atc_codes = [
    # "0",
    # "1",
    # "3",
    # "5", "6", "7",
    # "A",
    # "B",
    # "C",
    # "D",
    # "E", "G",
    # "H",
    # "J",
    # "K",
    # "L",
    # "M",
    # "N",
    # "P",
    # "Q",
    # "R",
    # "S",
    # "T", "V",
    "Z"
]

def get_text(elem):
    return elem.text.strip() if elem else ""

def scrape_atc(atc_code):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    print(f"Scraping ATC: {atc_code}")

    url = f"https://www.raviminfo.ee/apthkiri.php?apteek=?&regioon=01&atc={atc_code}"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
        )
    except:
        print(f"Timeout waiting for ATC {atc_code}")
        driver.quit()
        return None

    data = []
    page_number = 1

    while True:
        print(f"  Scraping page {page_number} for ATC {atc_code}")
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        valid_row_index = 0

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) < 10:
                continue
            if valid_row_index < 3:
                valid_row_index += 1
                continue

            apt_code = get_text(cols[0])
            name_elem = cols[1].find_elements(By.TAG_NAME, "a")
            name = get_text(name_elem[0]) if name_elem else get_text(cols[1])
            link = name_elem[0].get_attribute("href") if name_elem else ""
            atc = get_text(cols[2])
            orig_arv = get_text(cols[3])
            hind = get_text(cols[4])
            hind_kaart = get_text(cols[5])
            piirhind = get_text(cols[6])
            sood50 = get_text(cols[7])
            sood75 = get_text(cols[8])
            sood90 = get_text(cols[9])
            sood100 = get_text(cols[10])

            data.append([
                apt_code, name, link, atc, orig_arv, hind,
                hind_kaart, piirhind, sood50, sood75, sood90, sood100
            ])

        try:
            next_button = driver.find_element(By.LINK_TEXT, ">")
            next_button.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
            )
            page_number += 1
        except:
            break

    driver.quit()

    df = pd.DataFrame(data, columns=[
        "AptCode", "Nimetus", "Link", "ATC", "Orig. arv", "Hind",
        "Hind kl.kaardiga", "Piirhind", "Sood.h. (50%)",
        "Sood.h. (75%)", "Sood.h. (90%)", "Sood.h. (100%)"
    ])

    output_path = os.path.join(output_dir, f"medication_data_{atc_code}.csv")
    df.to_csv(output_path, index=False, encoding="utf-8")
    return output_path

def zip_csv_files(csv_files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in csv_files:
            zipf.write(file, os.path.basename(file))

if __name__ == "__main__":
    with Pool(processes=5) as pool:  # Set to 4 processes or adjust to your system
        csv_file_paths = pool.map(scrape_atc, atc_codes)

    csv_file_paths = [f for f in csv_file_paths if f]

    # Start zip operation in a separate thread
    zip_thread = threading.Thread(target=zip_csv_files, args=(csv_file_paths, "medication_data.zip"))
    zip_thread.start()
    zip_thread.join()

    print("Zipping complete.")
