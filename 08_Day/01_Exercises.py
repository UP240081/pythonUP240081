#1. 
dog = {}
#2.
dog = {'name':'dogo', 'color':'golden', 'breed':'golden retriever', 'legs':'4', 'age':'6'}
#3.
student = {'first_name':'damian', 'last_name':'Tinoco', 'gender':'Male', 'age':'18', 
           'marital status':'married', 'skills':['guitar', 'python', 'skate'], 'country':'Mexico', 
           'city':'Aguascalientes', 'address':'118 Vista del solsticio'}
#4.
print(len(student))
#5.
print(type(student['skills']))
#6.
student['skills'].append('html')
print(student)
#7.
print(student.keys())
#8.
print(student.values())
#9.
studenttpl = tuple(student.items())
print(studenttpl)
#10.
del student['last_name']
#11.
del dog