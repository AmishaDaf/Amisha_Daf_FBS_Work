# 8. Write a program to convert days into years, weeks and days.

n = int(input('Enter days: '))

year = n // 365
rem_days = n % 365
week = rem_days // 7
day = rem_days % 7

print(f'{year} Year, {week} Weeks and {day} days')
