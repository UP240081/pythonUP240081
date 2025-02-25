#Dia 2: programacion en python 
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
#---------------------------------------
print('Nombre:', nombre)
print('Apellido:', apellido)
print('Nombre completo:', nombre_completo)
print('Pais:', pais)
print('Ciudad:', ciudad)
print('Edad:', edad)
print('Año:', año)
print('Casado?:', is_married)
print(A, B)
#---------------------------------------
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type((A, B)))
print(len(nombre))
print(len(apellido))
#----------------------------------------
num_one = 5 
num_two = 4
total = num_one + num_two
diff = num_one - num_two 
product = num_one * num_two 
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print('4+5=',total)
print('4-5=',diff)
print('4*5=',product)
print('4/5=',division)
print('4%5=',remainder)
print('4**5=',exp)
print('4//5=',floor_division)
#-----------------------------------
radius = int(input('radius = '))
area_of_circle = 3.14 * (radius ** 2)
circumference = 2*3.14*radius
print(area_of_circle)
print(circumference)
#------------------------------------------
user_name = input('Name: ')
user_lastname = input('Last name: ')
user_country = input('Country: ')
age = input('age: ')
help('keywords')