import zipfile
import os
import pandas as pd
import tempfile

# === Configuration ===
zip_path = "medications.zip"            # Input ZIP file with CSVs
numbered_excel_output_path = "medications_numbers.xlsx"  # Output Excel file for numbered ATC codes
lettered_excel_output_path = "medications_letters.xlsx"  # Output Excel file for lettered ATC codes

# === Step 1: Extract ZIP to temporary directory ===
with tempfile.TemporaryDirectory() as temp_dir:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
        print(f"Extracted to: {temp_dir}")

    # === Step 2: Split CSVs into two Excel files (numbers vs letters) ===
    with pd.ExcelWriter(numbered_excel_output_path, engine='xlsxwriter') as num_writer, \
         pd.ExcelWriter(lettered_excel_output_path, engine='xlsxwriter') as let_writer:

        for file_name in os.listdir(temp_dir):
            if file_name.endswith(".csv"):
                csv_path = os.path.join(temp_dir, file_name)
                sheet_name = os.path.splitext(file_name)[0][:31]  # Max 31 characters for sheet name

                print(f"Adding sheet: {sheet_name}")

                # Read the CSV file
                df = pd.read_csv(csv_path, low_memory=False)

                # Replace the Link column with shortened text to avoid Excel hyperlink limit
                if "Link" in df.columns:
                    df["Link"] = df["Link"].apply(lambda x: "[link]" if pd.notna(x) and str(x).startswith("http") else x)

                # Determine if the last character of the sheet name is a number or a letter
                if sheet_name[-1].isdigit():  # If the last character is a digit (number)
                    df.to_excel(num_writer, sheet_name=sheet_name, index=False)
                else:  # If the last character is a letter
                    df.to_excel(let_writer, sheet_name=sheet_name, index=False)

print("✅ Excel files for numbered and lettered ATC codes have been saved.")
