#1.
def evens_odds_(n): 
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = sum(1 for i in range(n+1) if i % 2 != 0)
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_odds_(100))
#2.
def factorial(n): 
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    print('fact of', n, 'is', fact)
print(factorial(5))
#3.
def is_empty(value):
    return not bool(value)
print(is_empty(''))
#4.
def calculate_mean(lst):
    return int(sum(lst) / len(lst))
print(calculate_mean([2,3,4]))

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (sorted_lst[mid] if n % 2 != 0 else (sorted_lst[mid - 1] + sorted_lst[mid]) / 2)
print(calculate_median([2,3,4]))

def calculate_mode(lst):
    return max(set(lst), key=lst.count)
print(calculate_mode([2,3,4,4]))

def calculate_range(lst):
    return max(lst) - min(lst)
print(calculate_range([2,3,4]))

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
print(calculate_variance([2,3,4]))

def calculate_std(lst):
    import math
    return math.sqrt(calculate_variance(lst))
print(calculate_std([2,3,4]))