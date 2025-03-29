from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define function before map()
def double(num):
    return num * 2
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)

# Define function before filter()
def is_even(num):
    return num % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)

# Define function before reduce()
def multiply(x, y):
    return x * y
product = reduce(multiply, numbers)
print(product)

#4.
for country in countries:
    print(country)

#5.
for name in names:
    print(name)

#6.
for number in numbers:
    print(number)