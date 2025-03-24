#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(2))
#2
def all_unique(lst):
    return len(lst) == len(set(lst))
print(all_unique([4,4,4,4,5,5,5,6,7]))
#3
def all_same_type(lst):
    return all(isinstance(i, type(lst[0])) for i in lst)
print(all_same_type(['hi',2,'3.14']))
#4
def is_valid_variable(name):
    import re
    return bool(re.fullmatch(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))
print(is_valid_variable('Damian'))
#5
from collections import Counter
from countries_data import countries_d 

def most_spoken_languages(n=10):
    language_counter = Counter()
    
    for country in countries_d:
        for language in country['languages']:
            language_counter[language] += 1

    return language_counter.most_common(n)

def most_populated_countries(n=10):
    sorted_countries = sorted(countries_d, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]
print(most_spoken_languages(20))
print(most_populated_countries(20))