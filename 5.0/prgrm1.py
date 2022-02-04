class Customer:
    def getData(self,name,accno,t,amount):
        self.name=name
        self.accno=accno
        self.t=t
        self.amount=amount
    def deposit(self,d):
        self.amount=self.amount+d
    def withdraw(self,b):
        self.amount=self.amount-b    
    def display(self):  
        print("\n\tCUSTOMER DETAILS\t")
        print("|-----------------------------|")
        print("  Name:",self.name)
        print("  Account number:",self.accno)
        print("  Balance:",self.amount)
        print("  Account type:",self.t)
        print("|-----------------------------|\n")