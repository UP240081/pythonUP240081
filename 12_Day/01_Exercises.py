#1.
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choices(characters, k=6))
print(random_user_id())

#2.
import random
import string
def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    n_ids, ids = int(input()), int(input())
    for _ in range(ids):
        user_ids = ''.join(random.choices(characters, k=n_ids))
        print(user_ids) 
print(user_id_gen_by_user())

#3.
def rgb_color_gen ():
    random.randint(0,10)
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    print(f"rgb({r}, {g}, {b})")
print(rgb_color_gen())
