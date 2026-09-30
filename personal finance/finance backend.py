
import csv
from pathlib import Path

p = Path('expense.csv')


headers = ["type", "category", "amount", "name"]

if not p.exists():
    with open("expense.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()



while True:

    main = input("1.add expense\n2.remove expense\n3.Exit\n:")

    if main == "3":
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
              
              
              
              #remove function is working now add some more methods tomorrow se
