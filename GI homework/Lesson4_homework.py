# Add a list of elements to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)

print(sample_set)

# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']

long_names = []
short_names = []

for name in names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

print(long_names)
print(short_names)


# Given a list where each element is a year. Determine whether the given year is a leap year. If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]

for year in years_list:
    if year % 100 == 0:
        print(f'{year} NO')
    elif year % 4 == 0 or year % 400 == 0:
        print(f'{year} YES')
    else:
        print(f'{year} NO')


# Write a program that prompts the user for a string and checks if the string contains only unique characters.

user_input = str(input("insert a string: "))

unique = True
for i in range(len(user_input)):
    for j in range(i + 1, len(user_input)):
        if user_input[i] == user_input[j]:
            unique = False

print(unique)