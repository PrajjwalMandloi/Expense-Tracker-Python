import csv
import os
from datetime import datetime
import config
print(config.BUDGET)

from config import FILE_NAME, BUDGET 
# FILE_NAME = "expenses.csv"
# BUDGET = 0

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category", "Amount", "Description"])


def menu():

    print("\n" + "=" * 55)
    print("            EXPENSE TRACKER SYSTEM")
    print("-" * 55)
    print(f"Today's Date : {datetime.now().strftime('%d-%m-%Y')}")
    print("=" * 55)

    print("1.  Add Expense")
    print("2.  View Expenses")
    print("3.  Search Expense")
    print("4.  Update Expense")
    print("5.  Delete Expense")
    print("6.  Total Expense")
    print("7.  Set Budget")
    print("8. Dashboard")
    print("9. Exit")

    print("=" * 55)


    create_file()



from expense import *
from reports import *
from budget import *


from budget import load_budget

load_budget()



while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_expense()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        total_expense()

    elif choice == "7":
        set_budget()

    elif choice == "8":
        dashboard()


    elif choice == "9":
        print("\n" + "=" * 55)
        print("Thank you for using Expense Tracker 😊")
        print("Have a Great Day!")
        print("=" * 55)
        break

    else:
        print("Invalid Choice!")