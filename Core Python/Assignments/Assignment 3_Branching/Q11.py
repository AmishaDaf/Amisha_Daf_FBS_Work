# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

a1 = int(input('Enter age of person 1: '))
a2 = int(input('Enter age of person 2: '))
a3 = int(input('Enter age of person 3: '))
a4 = int(input('Enter age of person 4: '))
a5 = int(input('Enter age of person 5: '))

tp1 = int(input('Enter ticket amount for person 1: '))
tp2 = int(input('Enter ticket amount for person 2: '))
tp3 = int(input('Enter ticket amount for person 3: '))
tp4 = int(input('Enter ticket amount for person 4: '))
tp5 = int(input('Enter ticket amount for person 5: '))

#person 1
if(a1 < 12):
    discount = tp1 * (30/100)
    tot1 = tp1 - discount
    print('Total amount you need to pay is ', tot1)
elif(a1 > 59):
    discount = tp1 * (50/100)
    tot1 = tp1 - discount
    print('Total amount you need to pay is ', tot1)
else:
    tot1 = tp1
    print('You need to pay full fair ',tot1)

#person 2
if(a2 < 12):
    discount = tp2 * (30/100)
    tot2 = tp2 - discount
    print('Total amount you need to pay is ', tot2)
elif(a2 > 59):
    discount = tp2 * (50/100)
    tot2 = tp2 - discount
    print('Total amount you need to pay is ', tot2)
else:
    tot2 = tp2
    print('You need to pay full fair ',tot2)

#person 3
if(a3 < 12):
    discount = tp3 * (30/100)
    tot3 = tp3 - discount
    print('Total amount you need to pay is ', tot3)
elif(a3 > 59):
    discount = tp3 * (50/100)
    tot3 = tp3 - discount
    print('Total amount you need to pay is ', tot3)
else:
    tot3 = tp3
    print('You need to pay full fair ',tot3)

#person 4
if(a4 < 12):
    discount = tp4 * (30/100)
    tot4 = tp4 - discount
    print('Total amount you need to pay is ', tot4)
elif(a4 > 59):
    discount = tp4 * (50/100)
    tot4 = tp4 - discount
    print('Total amount you need to pay is ', tot4)
else:
    tot4 = tp4
    print('You need to pay full fair ',tot4)

#person 5
if(a5 < 12):
    discount = tp5 * (30/100)
    tot5 = tp5 - discount
    print('Total amount you need to pay is ', tot5)
elif(a5 > 59):
    discount = tp5 * (50/100)
    tot5 = tp5 - discount
    print('Total amount you need to pay is ', tot5)
else:
    tot5 = tp5
    print('You need to pay full fair ',tot5)


total = tot1 + tot2 + tot3 + tot4 + tot5

print('Total ticket amount is: ',total)