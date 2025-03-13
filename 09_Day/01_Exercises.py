#1.
my_age = 18  

user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - user_age} more years to learn to drive.")

#2.
if user_age > my_age:
    age_diff = user_age - my_age
    print(f"You are {age_diff} year{'s' if age_diff != 1 else ''} older than me.")
elif user_age < my_age:
    age_diff = my_age - user_age
    print(f"I am {age_diff} year{'s' if age_diff != 1 else ''} older than you.")
else:
    print("We are the same age.")

# Compare two numbers a and b
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")