# rev = 0
# temp = num
# cal = lambda num : d = temp % 10
# temp = temp // 10
# rev = rev * 10  + d
# print(cal(123))


a= int(input('Enter x: '))
b = int(input('Enter y: '))
c= int(input('Enter c: '))
cal = lambda a, b, c: a=c, c=a
print(cal(a, b, c))
