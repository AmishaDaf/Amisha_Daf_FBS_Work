# 5. WAP to calculate selling price of book based on cost price and discount.

cp = int(input('Enter cost price: '))
dis = int(input('Enter discount: '))

sp = cp * ((100-dis)/100)

print(f'Selling Price is {sp}')