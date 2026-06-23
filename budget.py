import csv
from datetime import datetime
from config import FILE_NAME
import config
config.BUDGET
print(config.BUDGET)



def load_budget():
    try:
        with open("budget.txt", "r") as file:
            config.BUDGET = float(file.read())
    except:
        config.BUDGET = 0



def set_budget():

    while True:
        try:
            config.BUDGET = float(input("Enter Monthly Budget: ₹"))

            with open("budget.txt", "w") as file:
                file.write(str(config.BUDGET))

            print("Budget Updated Successfully!")
            break

        except ValueError:
            print("Invalid Budget!")


def check_budget():

    total = 0

    current_month = datetime.now().strftime("%m-%Y")

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            expense_month = row[1][3:]

            if expense_month == current_month:

                total += float(row[3])

    print(f"\nCurrent Month Expense : ₹ {total}")


    if total <= config.BUDGET:
        remaining = config.BUDGET - total
        print(f"Remaining Budget : ₹{remaining}")

    else:
        exceeded = total - config.BUDGET
        print("\n⚠ WARNING Budget Exceeded!")
        print(f"Budget : ₹{config.BUDGET}")
        print(f"Exceeded Amount : ₹{exceeded}")



def get_current_month_expense():

    total = 0

    current_month = datetime.now().strftime("%m-%Y")

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            expense_month = row[1][3:]

            if expense_month == current_month:

                total += float(row[3])

    return total



def get_remaining_budget():

    total = get_current_month_expense()

    return config.BUDGET - total