# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input('Enter number of student: '))
tot_per = 0
for i in range(n):
    m1 = int(input("Enter marks of subject 1: "))
    m2 = int(input("Enter marks of subject 2: "))
    m3 = int(input("Enter marks of subject 3: "))
    m4 = int(input("Enter marks of subject 4: "))
    m5 = int(input("Enter marks of subject 5: "))
    tot_m = m1 + m2 + m3 + m4 + m5
    per = (tot_m / 500)*100
    print("Percentage =", per)

    tot_per = tot_per + per
avg = tot_per / n
print('Average percentage : ',avg)