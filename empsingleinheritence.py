# empolyee single inheritence

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("name:",self.name,"age:",self.age)

class employee(person):
    def details(self):
        print("employee class called")

emp1=employee("shivu",50)
emp1.display()

emp1.details()

emp2=employee("nikil",21)
emp2.display()

emp2.details()
print(emp1.age,emp2.name)