class student:
    college="amity university"

    def __init__(self,name):
        self.name=name

    def display(self):
        print("Name:",self.name)
        print("College:",student.college)

s1=student("shivu")
s2=student("Prathi")

s1.display()
s2.display()

