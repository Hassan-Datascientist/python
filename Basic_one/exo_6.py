# Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

numbers = input("Enter a sequence of comma-separated numbers: ")

list_numbers = numbers.split(',')
tuple_numbers = tuple(list_numbers)

print('List:', list_numbers)
print('Tuple:', tuple_numbers)
