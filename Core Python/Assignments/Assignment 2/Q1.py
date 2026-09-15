# 1. Convert the time entered in hh,min and sec into seconds.

hh = int(input('Enter hour: '))
min = int(input('Enter minutes: '))
sec = int(input('Enter seconds: '))

m1 = min*60
h1 = hh*3600

Tot_sec = sec + m1 + h1
print(f'Total seconds is: {Tot_sec} ')

