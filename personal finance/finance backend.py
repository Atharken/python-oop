
import csv
from pathlib import Path

p = Path('expense.csv')

headers = ["type", "category", "amount", "name"]


def summary():

    with open("expense.csv","r",newline="") as f:
      r = csv.DictReader(f)

      r1 = list(r)
      
      return f"total number of transactions are {len(r1)}"
            
         
def average():

  local = []
  exp = int(0)
  
  with open("expense.csv","r",newline="") as f:
      r = csv.DictReader(f)

      for i in r:
          if i['type'] == "expense":
              exp = exp + int(i['amount'])
              local.append(i)
      return f"average expense is {exp/len(local)}"

         
def average2():

  local = []
  inc = int(0)
  
  with open("expense.csv","r",newline="") as f:
      r = csv.DictReader(f)

      for i in r:
          if i['type'] == "income":
              inc = inc + int(i['amount'])
              local.append(i)
      return f"average income is {inc/len(local)}"
              
      




if not p.exists():
    with open("expense.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()



while True:

    main = input("1.add expense\n2.remove expense\n3.summary\n4.Exit\n:")

    if main == "4":
      
        break

    elif main == "1":

        type = ""

        typee = input("enter type\n1.expense\n2.income\n:")
        if typee == "1":
            type = "expense"
        elif typee == "2":
            type = "income" 
        category = input("enter category\n")
        amount = int(input("enter amount\n:"))
        name = input("enter name\n")

        expense = {
            "type": type,
            "category": category,
            "amount": amount,
            "name": name
        }

        with open("expense.csv", "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=headers)
            w.writerow(expense)

    elif main == "2":
        
        
        expenses = []

        with open("expense.csv", "r", newline="") as f:
            r = csv.DictReader(f)

            for index, item in enumerate(r):
                print(
                    f" -- {index+1} type : {item['type']}  |  "
                    f"category : {item['category']}  |  "
                    f"amount : {item['amount']}  |  "
                    f"name : {item['name']}  "
                )
                expenses.append(item)

        remove = int(input("enter your expense to remove\n:"))
        expenses.pop(remove - 1)
        

        with open("expense.csv", "w", newline="") as f:
              w = csv.DictWriter(f,fieldnames = headers)
              w.writeheader()
              w.writerows(expenses)
    
    elif main == "3":

        print("===summary===")
        print(f"{summary()} \n{average()} \n{average2()}")


              
              
              
              #add search by category
