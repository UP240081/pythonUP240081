#1.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)    

#2.
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for item in sublist for item in item]
print(flattened_list)

#3.
tuples_list = [(i, *[i**j for j in range(6)]) for i in range(11)]
print(tuples_list)

#4.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[country.upper(), country[:3].upper(), city.upper()] 
                        for sublist in countries for (country, city) in sublist]
print(formatted_countries)

#5.
countries_dict_list = [{'country': country.upper(), 'city': city.upper()} 
                        for sublist in countries for (country, city) in sublist]
print(countries_dict_list)

#6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for sublist in names for name in sublist]
print(concatenated_names)

#7.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda x1, y1, m: y1 - m * x1 if m is not None else None
m = slope(1, 2, 3, 4)  
b = y_intercept(1, 2, m) 
print(f"Slope: {m}, Y: {b}")

