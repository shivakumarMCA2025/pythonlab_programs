class tele:
    def showme(self):
        print("dont stop")

class tele2(tele):
    def showme2(self):
        print("never stop")

class tele3(tele2):
    def showme3(self):
        print(" unstoppable")

obj=tele3()
obj.showme()
obj.showme2()
obj.showme3()

