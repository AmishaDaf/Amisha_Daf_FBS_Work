# 7. Write a program to check if user has entered correct userid and password.

uid = 'abc@123'
pw = 1234

id = (input("Enter user id: "))
pd = int(input('Enter password: '))

if(uid == id and pw == pd):
    print('User entered valid userid and passsword')
else:
    print('Invalid userid and password')