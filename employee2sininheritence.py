class employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id


    def details(self):
        print("name:",self.name,"emp_id:",self.emp_id)

class emp2(employee):
    def __init__(self,name,emp_id,domain):
        employee.__init__(self,name,emp_id)
        self.domain=domain

    def show_domain(self):
        print("emp detials")

dev1=emp2("shivu",21,"py")
dev2=emp2("char",23,"c++")
dev1.details()
dev2.details()

dev1.show_domain()