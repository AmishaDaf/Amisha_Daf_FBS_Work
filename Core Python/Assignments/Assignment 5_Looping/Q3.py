# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n= int(input('Enter number of passenger: '))
for i in range(n):
    age = int(input('Enter passenger age: '))
    t = int(input('Enter ticket cost: '))
    
    if(age < 12):
        dis = t * (30/100)
        tot1 = t - dis
        print('Ticket cost is ', tot1)
    elif(age > 59):
        dis = t * (50/100)
        tot2 = t - dis
        print('Ticket cost is ',tot2)
    else:
        tot3 = t
        print('Ticket cost is ', tot3)

tot_amt = tot1 + tot2 + tot3
print("Total amount of all passenger is", tot_amt)