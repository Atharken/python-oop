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
  main = int(input("======BANK======\n\n1.Create account\n2.Deposit\n3.Withdraw\n4.Check balance\n5.Account information\n6.Show all account\n7.Exit\n:"))
  if main == 7:
      print("thanks for using our code")
      break

  
  elif main == 1:
    name = input("enter your name\n:")
    y = bankaccount(name)
    accounts.append(y)


  elif main == 2:
    acc = input("enter account owner name\n:")
    for i in accounts:
       if i.owner == acc:     # think of i as a bankaccount(athar) not a string but a whole class 
          x = int(input("enter your amount\n:"))
          i.deposit(x)


  elif main == 3:
    acc = input("enter account owner name\n:")
    for i in accounts:
      if i.owner == acc:     # think of i as a bankaccount(athar) not a string but a whole class 
        x = int(input("enter your amount\n:"))
        i.withdraw(x)

  elif main == 4:
    acc = input("enter account owner name\n:")
    for i in accounts:
      if i.owner == acc:
       x1 = i.check_balance()
       print(x1)
           
  
  elif main == 5:
    acc = input("enter account owner name\n:")
    for i in accounts:
      if i.owner == acc:
       x1 = i.check_balance()
       print(x1)

  elif main == 6:
     for i in accounts:
        x = i.check_balance()
        print(f"{x}\n\n\n")
           