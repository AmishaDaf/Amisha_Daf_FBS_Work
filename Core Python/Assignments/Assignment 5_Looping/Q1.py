# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.




for i in range(1, 5):
    id = (input('Enter User id: '))
    pw = int(input('Enter Password: '))
    if(id == 'admin' and pw == 1234):
        print('Login Successful')
        break
    else:
        print('Enter credential again')
else:
    print('Invalid credentials')
