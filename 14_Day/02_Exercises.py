from functools import reduce
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Use map() to change each country to uppercase
uppercase_countries = list(map(lambda country: country.upper(), countries))
print("Uppercase Countries:", uppercase_countries)

# 2. Use map() to square each number
squared_numbers = list(map(lambda num: num ** 2, numbers))
print("Squared Numbers:", squared_numbers)

# 3. Use map() to change each name to uppercase
uppercase_names = list(map(lambda name: name.upper(), names))
print("Uppercase Names:", uppercase_names)

# 4. Use filter() to filter out countries containing "land"
land_countries = list(filter(lambda country: 'land' in country.lower(), countries))
print("Countries containing 'land':", land_countries)

# 5. Use filter() to filter out countries having exactly six characters
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
print("Countries with exactly six characters:", six_char_countries)

# 6. Use filter() to filter out countries containing six or more letters
six_or_more_countries = list(filter(lambda country: len(country) >= 6, countries))
print("Countries with six or more characters:", six_or_more_countries)

# 7. Use filter() to filter out countries starting with an 'E'
e_countries = list(filter(lambda country: country.startswith('E'), countries))
print("Countries starting with 'E':", e_countries)

# 8. Chain two or more list iterators (map, filter, reduce)
chained_result = reduce(lambda x, y: x + ', ' + y,
                        filter(lambda country: len(country) >= 6,
                               map(lambda country: country.upper(), countries)))
print("Chained result (Uppercase & filtered countries):", chained_result)

# 9. Define a function to filter only string items from a list
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

# Example usage
mixed_list = ['Python', 123, 'Hello', 3.14, 'World', True]
string_list = get_string_lists(mixed_list)
print("Filtered string list:", string_list)

# 10. Use reduce() to sum all numbers in numbers list
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

# 11. Use reduce() to concatenate all countries into a sentence
sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.'
print("Concatenated Sentence:", sentence)

#12.
def categorize_countries(pattern):
    return [country for country in countries if pattern.lower() in country.lower()]
print("Countries containing 'land':", categorize_countries('land'))

#13.
def country_name_count():
    country_dict = {}
    for country in countries:
        first_letter = country[0].upper()
        country_dict[first_letter] = country_dict.get(first_letter, 0) + 1
    return country_dict
print("Country count by first letter:", country_name_count())

#14.
def get_first_ten_countries():
    return countries[:10]
print("First 10 countries:", get_first_ten_countries())

#15.
def get_last_ten_countries():
    return countries[-10:]
print("Last 10 countries:", get_last_ten_countries())



