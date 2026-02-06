class student:
    college = "ABC"
    def __init__(self, name,age):
        self.name = name
        self.age=age
    def display(self):   # fixed spelling
        print("Name:", self.name,"Age:",self.age)
        print("College name:", student.college)
s1 = student("shivu",21)
print("college name",student.college)
s1.name="prety"
s1.age=21
print("student",s1.name,s1.age)
student.college="ABC"
print("college name:",student.college)
s1.display()


