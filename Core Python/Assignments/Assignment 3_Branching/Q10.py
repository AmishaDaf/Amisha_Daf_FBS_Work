# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gen = (input('Enter gender (F/M): '))
age =int(input('Enter age: '))

if(gen == 'F'):
    if(age>=18):
        print('Girl is Eligible for marriage')
    else:
        print('Girl is not eligible for marriage')
elif(gen == 'M'):
    if(age>=21):
        print('Boy is Eligible for marriage')
    else:
        print('Boy is not eligible for marriage')
else:
    print('Invalid Gender') 
