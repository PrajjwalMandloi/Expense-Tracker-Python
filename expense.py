import csv
from datetime import datetime
from config import FILE_NAME
from budget import check_budget
import config
print(config.BUDGET)

def generate_expense_id():

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) == 1:
            return 1
            
        last_id = int(rows[-1][0])

        return last_id + 1

    

def add_expense():

    category = input("Enter Category: ")

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Please enter a valid amount!")

    description = input("Enter Description: ")

    date = datetime.now().strftime("%d-%m-%Y")

    # Auto Generate ID
    expense_id = generate_expense_id()

    # Save Data
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, date, category, amount, description])

    print("\nExpense Added Successfully!\n")
    check_budget()



def view_expenses():

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("\nNo Expenses Found!\n")
            return

        print("\n" + "-" * 75)
        print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
        print("-" * 75)

        for row in rows[1:]:     
            print(f"{row[0]:<5}{row[1]:<15}{row[2]:<15}{row[3]:<12}{row[4]}")

        print("-" * 75)



def search_expense():

    category = input("Enter Category to Search: ").title()

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n" + "-" * 75)
        print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
        print("-" * 75)

        next(reader)  

        for row in reader:
            if row[2].strip().lower() == category.strip().lower():
                print(f"{row[0]:<5}{row[1]:<15}{row[2]:<15}{row[3]:<12}{row[4]}")
                found = True

        print("-" * 75)

    if not found:
        print("No Expense Found!")



def update_expense():

    expense_id = input("Enter Expense ID to Update: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] == expense_id:

                print("\nCurrent Details")
                print("-----------------------")
                print("Category :", row[2])
                print("Amount :", row[3])
                print("Description :", row[4])

                print("\nEnter New Details")

                row[2] = input("New Category: ").strip().title()

                while True:
                    try:
                        row[3] = float(input("New Amount: "))
                        break
                    except ValueError:
                        print("Invalid Amount!")

                row[4] = input("New Description: ")

                found = True

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("\nExpense Updated Successfully!")

    else:
        print("\nExpense ID Not Found!")


def delete_expense():

    expense_id = input("Enter Expense ID to Delete: ")

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] == expense_id:
                found = True
                continue    

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("\nExpense Deleted Successfully!")

    else:
        print("\nExpense ID Not Found!")

