class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0<=marks<=100:

            self.__marks=marks
        else:
            print("invalid num")

s=student("shivu",99)

print("name:",s.get_name())
print("marks:",s.get_marks())

s.set_marks(79)
print("updated:",s.get_marks())