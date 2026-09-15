# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input('Enter electricity unit: '))

if(unit <= 50):
    bill = unit * 0.50
elif(unit <= 150):
    d = unit - 50
    t1 = 50 * 0.50
    t2 = d * 0.75
    bill = t1 + t2
elif(unit <= 250):
    d = unit - 50
    d1 = d - 100
    t1 = 50 * 0.50
    t2 = 100 * 0.75
    t3 = d1 * 1.20
    bill = t1 + t2 + t3
else:
    d = unit - 50
    d1 = d - 100
    d2 = d1 - 100
    t1 = 50 * 0.50
    t2 = 100 * 0.75
    t3 = 100 * 1.20
    t4 = d2 * 1.50
    bill = t1 + t2 + t3 + t4

surcharge = bill * (20/100)

total = bill + surcharge

print('Total bill : ',total)