# Print to console what is different in each set compared to another
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.difference(set_b))
print(set_b.difference(set_a))

# Create a string from a list and save it to variable
# Make each name on a new line.
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
names_string = '\n'.join(names)
print(names_string)

# string = ''
#
# for name in names:
#     string += name + '\n'
#
# print(string)

# print sum of all numbers in a list
# print sum of all unique numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
print(sum(numbers))
print(sum(set(numbers)))

# sum=0
# for number in numbers:
#     sum += number
# print(sum)
#
# unique_nr=list(set(numbers))
#
# sum_u=0
# for number in unique_nr:
#     sum_u += number
# print(sum_u)

# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']

new_list=list(set(studentsA + studentsB))
print(new_list)

# What elements are common for both tuples?
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)

print(set(numbersA).intersection(set(numbersB)))

# A_set=set(numbersA)
# B_set=set(numbersB)
#
# print(A_set.intersection(B_set))

# add 5 to the tuple on a right position
a = (1, 2, 3, 4, 6, 7, 8)
b = a[:4] + (5,) + a[4:]
print(b)

c = list(a)
c.append(5)
c.sort()
c = tuple(c)
print(c)

# a_list = list(a)
# a_list.insert(4, 5)
# print(tuple(a_list))