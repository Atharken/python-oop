class bankaccount:

    
    def __init__(self, owner):
        self.owner = owner
        self.balance = 10000



    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance 

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    def check_balance(self):
        return f"name : {self.owner}\nbalance : {self.balance}"


accounts = []
while True:

  name = input("enter your name\n:")
  if name == "exit":
      print(accounts)
      break
  bal = int(input("enter your amount\n:"))

  y = bankaccount(name)
  accounts.append(y)
  x = y.deposit(bal)
  p1 = y.owner

  x2 = y.check_balance()
  print(accounts)

  
  print(x2)