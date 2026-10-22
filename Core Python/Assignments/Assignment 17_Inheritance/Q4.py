# Create a class College which has collection of students. Add the following methods : 
# a. Parameteried constructor for number of students. 
# b. AddStudent 
# c. GetStudent 
# d. RemoveStudent 
# e. Override __str__ Method


class Student:
    def __init__(self, id, name, age, per):
        self.id = id
        self.name = name
        self.age = age
        self.per = per

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Percentage: {self.per}"


class College:
    def __init__(self, n):
        self.capacity = n
        self.students = []

    def AddStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print(f"Student {student.id} added successfully")
        else:
            print("College is full")

    def GetStudent(self, sid):
        for student in self.students:
            if student.id == sid:
                return student

        return "Student not found"

    def RemoveStudent(self, sid):
        for student in self.students:
            if student.id == sid:
                self.students.remove(student)
                print(f"Student {student.id} removed successfully")
                return

        print("Student not found")

    def __str__(self):
        result = "College Student Details:\n"

        if len(self.students) == 0:
            return "No students available"

        for student in self.students:
            result = result + str(student) + "\n"

        return result


# Create Student objects
s1 = Student(101, "Amisha", 21, 85)
s2 = Student(102, "Rahul", 22, 78)
s3 = Student(103, "Priya", 20, 90)

# Create College object with capacity 3
c1 = College(3)

# Add students
c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)

# Display all students
print(c1)

# Get a student by ID
print("Search Result:", c1.GetStudent(102))

# Remove a student by ID
c1.RemoveStudent(102)

# Display students after removal
print(c1)
