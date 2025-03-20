#1.
total_sum = 0
for i in range(101):
    total_sum += i
print("The sum of all numbers is", total_sum)
#2.
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("The sum of all evens is", even_sum)
print("The sum of all odds is", odd_sum)

