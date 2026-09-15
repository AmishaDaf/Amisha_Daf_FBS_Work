# 3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

f_m = feet * 0.3048
f_cm = feet * 30.48

i_cm = inches * 2.54
i_m = inches * 0.0254

print(f'Feet in meter is {f_m} and in centimeter is {f_cm}')
print(f'Inches in meter is {i_m} and in centimeter is {i_cm}')