#1.
empty_list = list()
#2.
lst = ['1', '2', '3', '4', '5']
print(len(lst)) #3.
#4.
print(lst[0])
print(lst[2])
print(lst[4])
#5.
mixed_data_types = ['Damian', '18', '1.73', 'Married', 'Lomas de Vistabella 2da seccion']
print(mixed_data_types)
#6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)#7.
print(len(it_companies))#8
#9.
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
#10.
it_companies[0] = 'Twitter'
print(it_companies)
#11. 
it_companies.insert(1, 'Arduino')
print(it_companies)
#12.
it_companies.insert(4, 'Youtube')
print(it_companies)
#13. 
it_companies[3]= 'MICROSOFT'
print(it_companies)
#14.
it_str= '#; '.join(it_companies)
print(it_str)
#15.
print('MICROSOFT' in it_companies)
#16
print(sorted(it_companies))
#17.
it_companies.sort(reverse=True)
print(it_companies)
#18
del it_companies [0:2]
print(it_companies)
#19
del it_companies [4:6]
print(it_companies)
#20
del it_companies [1]
print(it_companies)
#21
del it_companies[0]
print(it_companies)
#22
del it_companies[0]
print(it_companies)
#23
del it_companies[1]
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
end = front_end + back_end
print(end)
#27
Full_Stack = end.copy()
Full_Stack.insert(5, 'Python')
Full_Stack.insert(5, 'SQL')
print(Full_Stack)
