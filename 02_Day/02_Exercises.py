#Dia 2: programacion en python LEVEL 2
nombre = 'Jose Damian'
apellido = 'Mendez Tinoco'
nombre_completo = 'Jose Damian Mendez Tinoco'
pais = 'Mexico'
ciudad = 'Aguascalientes'
edad = 18
año = 2025
is_married = 'true'
is_true = 'true'
A, B = 'HOLA', 'ADIOS'
#------------------------------------------------------
print(type(nombre)) #1.Check the data type of all your variables using type() built-in function
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type((A, B)))
print(len(nombre)) #2.Using the len() built-in function, find the length of your first name
print(len(apellido)) #3.Compare the length of your first name and your last name
#----------------------------------------
num_one = 5 #4.Declare 5 as num_one and 4 as num_two
num_two = 4
total = num_one + num_two #5.Add num_one and num_two and assign the value to a variable total
diff = num_one - num_two #6.Subtract num_two from num_one and assign the value to a variable diff
product = num_one * num_two #7.Multiply num_two and num_one and assign the value to a variable product
division = num_one / num_two #8.Divide num_one by num_two and assign the value to a variable division
remainder = num_one % num_two #9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exp = num_one ** num_two #10.Calculate num_one to the power of num_two and assign the value to a variable exp
floor_division = num_one // num_two #11.Find floor division of num_one by num_two and assign the value to a variable floor_division
print('4+5=',total)
print('4-5=',diff)
print('4*5=',product)
print('4/5=',division)
print('4%5=',remainder)
print('4**5=',exp)
print('4//5=',floor_division)
#-----------------------------------
#12.The radius of a circle is 30 meters.
#i.Calculate the area of a circle and assign the value to a variable name of area_of_circle
#ii.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#iii.Take radius as user input and calculate the area.
radius = int(input('radius = '))
area_of_circle = 3.14 * (radius ** 2)
circumference = 2*3.14*radius
print(area_of_circle)
print(circumference)
#------------------------------------------
#13.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_name = input('Name: ')
user_lastname = input('Last name: ')
user_country = input('Country: ')
age = input('age: ')
help('keywords') #14.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords