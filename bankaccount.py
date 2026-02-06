#create class bank account having data memebers customer , balance.
#protrct data members and perform following deposite withdraw,get balance

class bank_account:
    def __init__(self,customer,balance):
        self.__customer=customer
        self.__balance=balance

    def deposite(self,amount):
        if amount>0:
            self.__balance+=amount

        else:
            print("invalid deposite")


    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else:
            print("invalid amount")

    def get_balance(self):
        return self.__balance

c1=bank_account("shivu",1100)

c1.deposite(100)
c1.withdraw(50)

print("current balance:",c1.get_balance())
