# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1 = int(input('Enter subject 1 marks: '))
s2 = int(input('Enter subject 2  marks: '))
s3 = int(input('Enter subject 3 marks: '))
s4 = int(input('Enter subject 4 marks: '))
s5 = int(input('Enter subject 5 marks: '))

per = ((s1 + s2 + s3 + s4 + s5)/500)*100
if(s1<= 100 and s2<= 100 and s3<= 100 and s4<= 100 and s5<= 100):
    if(per >= 75):
        print('First class with distinction')
    elif(per >= 60):
        print('First class')
    elif(per >= 50):
        print('Second class')
    elif(per >= 35):
        print('Pass')
    else:
        print('Fail')
else:
    print('Invalid marks')