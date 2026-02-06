
class University:
    def set_university(self):
        self.university_name = input("Enter university name: ")

class Department(University):
    def set_department(self):
        self.dept_name = input("Enter department name: ")

class Student(Department):
    def set_student(self):
        self.student_name = input("Enter student name: ")

    def display(self):
        print("\n--- Details ---")
        print("University name:", self.university_name)
        print("Department name:", self.dept_name)
        print("Student name:", self.student_name)

# Object creation
s = Student()
s.set_university()
s.set_department()
s.set_student()
s.display()