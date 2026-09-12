class bankaccount:

    
    def __init__(self, owner, id):
        self.owner = owner
        self.balance = 10000
        self.id = id



    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance 

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def check_balance(self):
        return f"name : {self.owner}\nbalance : {self.balance}"

    def acc_info(self):
        return f"name : {self.owner}\nbalance : {self.balance}\naccount id : {self.id}"
    
    


accounts = []
while True:
  main = int(input("======BANK======\n\n1.Create account\n2.Deposit\n3.Withdraw\n4.Check balance\n5.Account information\n6.Show all account\n7.Exit\n:"))
  if main == 7:
      print("thanks for using our code")
      break

  
  elif main == 1:
    name = input("enter your name\n:")
    x = 1001
    
    found = True
    for i in accounts:
      if i.owner == name:
        found = False
        print("account name already existed")
        break
    if found == False:
      continue


    if len(accounts) >= 0:
      t = x
      for i in accounts:
        if i.id >= t:
          t = t + 1
        x = t
          
    
    y = bankaccount(name, x)
    accounts.append(y)  #account object is stored in a list


  elif main == 2:
    acc = input("enter account owner name\n:")
    found = False
    for i in accounts:
      if i.owner == acc:   # think of i as a bankaccount(athar) not a string but a whole class
        found = True
        try: 
          x = int(input("enter your amount\n:"))
          if x <= 0:
            print("you can't deposit amount less than or equal to 0")
            continue
        except ValueError:
          print("enter a valid number")
          continue
        else:
        
          i.deposit(x)
        break
    if found == False: 
      print(f"no account found of name {acc}")
      continue


  elif main == 3:
    acc = input("enter account owner name\n:")
    found = False
    for i in accounts:
      if i.owner == acc:     # think of i as a bankaccount(athar) not a string but a whole class 
        found = True
        try:
          x = int(input("enter your amount\n:"))
        except ValueError:
          print("enter a valid number ! ! !")
          continue
        else:
          if x > i.balance:
            print("insufficient balance")
            continue
          i.withdraw(x)
          break
    if found == False: 
      print(f"no account found of name {acc}")
      continue


  elif main == 4:
    acc = input("enter account owner name\n:")
    found = False
    for i in accounts:
      if i.owner == acc:
       found = True
       x1 = i.check_balance()
       print(x1)
    if found ==  False: 
      print(f"no account found of name {acc}")
      continue
  
  
  elif main == 5:
    acc = input("enter account owner name\n:")
    found = False
    for i in accounts:
      if i.owner == acc:
       found = True
       x1 = i.acc_info()
       print(x1)
    if found == False: 
      print(f"no account found of name {acc}")
      continue
  


  elif main == 6:
     for i in accounts:
        x = i.acc_info()
        print(f"{x}\n\n\n")
           