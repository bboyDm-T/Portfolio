"""
Task:
You have two lists: one containing names of students and another containing their corresponding scores.
Create a dictionary where the names are the keys and the scores are the values using zip().
"""

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 88]

zipped = dict(zip(students, scores))

print(zipped)

'''
Task:
You have a list of product prices in dollars. Convert them to euros using a given conversion rate (1 USD = 0.85 EUR).
Use map() to perform the conversion.
'''

usd_prices = [100, 150, 200, 250, 300]
conversion_rate = 0.85

eur_prices = list(map(lambda x: x * conversion_rate, usd_prices))

print(eur_prices)

'''
Task:
You have a list of ages. Use filter() to create a new list containing only the ages that are 18 or older.
'''

ages = [12, 17, 19, 24, 15, 30, 16, 18]

ages18 = list(filter(lambda x: x >= 18, ages))

print(ages18)

'''
Task:
Given a dictionary of products and their prices, increase all prices by 10% using dictionary comprehension.
'''

products = {
    "Laptop": 1000,
    "Smartphone": 800,
    "Tablet": 500,
    "Headphones": 200
}

for key in products:
    products[key] = int(products[key] * 1.1)

print(products)

'''
Task:
You have a list of numbers. 
- First, use a list comprehension to square all the numbers.
- Then, use filter() to extract only the squared numbers that are greater than 50.
'''

numbers = [3, 5, 7, 9, 11]

sq_nr = [num ** 2 for num in numbers]

filtered_nrs = list(filter(lambda x: x > 50, sq_nr))

print(filtered_nrs)