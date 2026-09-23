# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

c = int(input('Enter temperature in celsius: '))

f = (c * (9/5)) + 32

print(f'Temperature in fahrenheit is: {f} F')