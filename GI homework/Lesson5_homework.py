# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number

def square(list):
    new_list = []
    for item in list:
        new_list.append(item ** 2)
    return new_list

test_list = [1, 2, 3]
print(square(test_list))

# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens

def amount(list):
    odd = 0
    even = 0
    for number in list:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return (odd, even)

print(amount([1, 2, 3, 4, 5]))

# Write a function that accepts a list of numbers
# and returns largest number

def largest(list):
    return max(list)

somenr = [1, 99, 8]

print(largest(somenr))

# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)

def fb(start, end):
    for num in range(start, end+1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')

fb(0, 15)