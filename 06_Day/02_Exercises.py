sisters = ('Minerva', 'Mila')
brothers = ('Dennis', )
siblings = brothers + sisters
parents = ('Jose', 'Carla')
Familiy_members = parents + siblings
#1. 
print(Familiy_members)
momma, dada, *sibs = Familiy_members
print(sibs)
print(momma)
print(dada)
#2.
fruits = ("watermelon", "banana", "kiwi")
vegetables = ("carrot", "broccoli", "onion")
animal_products = ("milk", "cheese", "butter")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3.
food_stuff_lt = list(food_stuff_tp)
#4.
middle_item_tuple = food_stuff_tp[len(food_stuff_tp) // 2]
print(middle_item_tuple) 
#5.
print(food_stuff_lt [2:6])
#6.
del(food_stuff_tp)
#7.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)