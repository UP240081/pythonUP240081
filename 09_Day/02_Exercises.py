#1.
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
else:
    print("Grade: F")

#2. 
month = input("Enter a month: ").lower()
if month in ['september', 'october', 'november']:
    print("Season: Autumn")
elif month in ['december', 'january', 'february']:
    print("Season: Winter")
elif month in ['march', 'april', 'may']:
    print("Season: Spring")
elif month in ['june', 'july', 'august']:
    print("Season: Summer")
else:
    print("Invalid month")
#3.
    fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if (new_fruit in fruits):
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruit)
    print("Modified fruit list:", fruits)