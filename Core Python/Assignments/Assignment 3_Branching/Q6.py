# 6. Write a program to calculate profit or loss.

sp = int(input('Enter selling price: '))
cp = int(input('Enter cost price: '))
profit = sp - cp
loss = cp - sp
if(sp > cp):
    print("User make profit of rs: ",profit)
else:
    print('User make loss of rs: ', loss)