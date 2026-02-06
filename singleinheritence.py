#single inheritence

class p:
    def fun1(self):
        print("parents class")

    def fun3(self):
        print("hello")

class c(p):
    def fun2(self):
        print("child class")

obj=c()
obj.fun1()
obj.fun2()
obj.fun3()