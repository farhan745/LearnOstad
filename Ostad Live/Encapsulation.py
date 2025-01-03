class BankAccount:
    __balance = 0

    #Deposit
    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount
            print("Deposit Success")
        else:
            print("Invalid Amount")
    #Withdraw
    def withdraw(self,amount):
        if amount>0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Success")
        else:
            print("Insufficient Balance")

    #check Balance
    @property
    def checkBalance(self):
        return self.__balance

obj = BankAccount()
obj.deposit(500)
print(obj.checkBalance)
obj.withdraw(400)
print(obj.checkBalance)