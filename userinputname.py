class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("name:",self.name," and is Age:",self.age)

name=input("enter your name:")
age=input("enter your age")

S=student(name,age)
S.show()



