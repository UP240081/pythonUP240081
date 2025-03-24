#1.
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))
#2.

def area_of_circle(r):
    area = 3.14159 * r * r
    return area
print(area_of_circle(2))
#3.
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All items must be numbers"
print(add_all_nums(1,2,5,6,7,8,9,10))
#4.
def c_F(cel):
    Far = (cel * 9/5) + 32
    return (Far)
print(c_F(30))
#5.
def check_season(month):
    seasons = {
    "Winter": ["December", "January", "February"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"],
    "Autumn": ["September", "October", "November"]
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Invalid month"
print(check_season('September'))
#6.
def calculate_slop(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slop(1, 2, 20, 4))
#7.
def solve_quadratic_eqn(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No Real Solutions"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        return ((-b + math.sqrt(discriminant)) / (2*a), (-b - math.sqrt(discriminant)) / (2*a))
print (solve_quadratic_eqn(80, 90, 2))
#8.
def print_list(lst):
    for item in lst:
     print(item)

print(print_list(['1','2','3']))
#9.
def reverse_list(lst):
    return lst[::-1]
print(reverse_list(['c','b','a']))
#10.
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
print(capitalize_list_items(['hi','goodbye']))
#11.
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(['hi', 'goodbye'], 'hello'))
#12.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print(remove_item(['hi', 'goodbye'], 'hi'))
#13.
def sum_of_numbers(n):
    return sum(range(n+1))
print (sum_of_numbers(41))
#14.
def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)
print(sum_of_odds(41))
#15.
def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)
print(sum_of_even(251))
