# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.


s1 = int(input('Enter subject 1 marks: '))
s2 = int(input('Enter subject 2  marks: '))
s3 = int(input('Enter subject 3 marks: '))
s4 = int(input('Enter subject 4 marks: '))
s5 = int(input('Enter subject 5 marks: '))

obtained_marks = s1 + s2 + s3 + s4 + s5
per = (obtained_marks/500)*100

print(f'Percentage is {per}')