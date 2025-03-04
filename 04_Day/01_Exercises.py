#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
cadena1 = 'thirty '+'days '+'of '+'python'
print(cadena1)
#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
cadena2 = 'coding '+'for '+'All'
print(cadena2)
#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "coding for all"
print(company)#4. Print the variable company using print().
print(len(company))#5.Print the length of the company string using len() method and print().
print(company.upper())#6.Change all the characters to uppercase letters using upper() method.
print(company.lower())#7.Change all the characters to lowercase letters using lower() method.
#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.    
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9. Cut(slice) out the first word of Coding For All string.
first_word = company [7:14]
print(first_word)
#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
company1 = 'Coding For All'
print(company1.index('Coding'))
#11. Replace the word coding in the string 'Coding For All' to Python.
print(company1.replace('Coding', 'Python'))
#12. Change Python for Everyone to Python for All using the replace method or other methods.
pfe = 'Python For Everyone'
print(pfe.replace('Everyone', 'All'))
#13. Split the string 'Coding For All' using space as the separator (split()) .
cfa = 'Coding For All'
print(cfa.split(' '))
#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
fgma = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (fgma.split(','))
#15. What is the character at index 0 in the string Coding For All.
print(cfa [0])
#16. What is the last index of the string Coding For All.
print(cfa [13])
#17. What character is at index 10 in "Coding For All" string.
print(cfa [9])
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
pyfoe = 'Python For Everyone'
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
cofa = 'Coding For All'
#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(cofa.index('C'))
#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(cofa.index('F'))
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(cofa.rfind('l'))
#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('you cannot end a sentence with because because because is a conjuction'.index('because'))
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('you cannot end a sentence with because because because is a conjuction'.rindex('because'))
#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' 
print('you cannot end a sentence with because because because is a conjuction'.replace('because',''))
#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('you cannot end a sentence with because because because is a conjuction'.index('because'))
#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' 
print('you cannot end a sentence with because because because is a conjuction'.replace('because',''))
#28. Does ''Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding'))
#29. Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('Coding'))
#30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
slc = '   Coding For All      '
cfa1= slc [3:17]
print(cfa1)
#31. 
challenge1='30DaysOfPython'
challenge2='thirty_days_of_python'
print(challenge1.isidentifier())
print(challenge2.isidentifier())
#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result1 = '# '.join(list)  
print(result1)
#33. 
print('i am enjoying this challenge\ni just wonder what is next')
#34.
print ('name\tage\tcountry\tcity\nasabaneh\t250\tFinland\tHelsinki')
#35.
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {}.'.format(radius, area) 
print(formated_string)
#36.
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))