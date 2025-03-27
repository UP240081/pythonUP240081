import random
#1.
def shuffle_list(lst):
    random.shuffle(lst)  
    return lst
print(shuffle_list([1, 8, 3, 0, 5]))  
#2.
def unique_random_number():
    numbers = []
    for _ in range(7): 
        num = random.randint(0, 9)
        while num in numbers:  
            num = random.randint(0, 9)
        numbers.append(num)  
    return numbers
print(unique_random_number())