import csv
from pathlib import Path

p = Path('expense.csv')


headers = ["type","category","amount","name"]
if not p.exists():
    with open("expense.csv","w",newline ="") as f:
        w = csv.DictWriter(f, fieldnames = headers)       
        w.writeheader()
        
expenses = []


while True:
    
    main = input("1.add expense\n2.remove expense\n3.Exit")
    
    
    if main == "3":
        break
        
        
    elif main == "1":
        
        type = input("enter type\n:")
        category = input("enter category\n")
        amount = int(input("enter amount\n:"))
        name = input("enter name\n")
        
        expense = {
            "type" : type,
            "category" : category,
            "amount" : amount,
            "name" : name
        }
        
        expenses.append(expense)
        
        with open("expense.csv","a",newline="") as f:
            w = csv.DictWriter(f, fieldnames=headers)
            w.writerow(expense)
        
         
        
        
print(expenses)
        
        
    