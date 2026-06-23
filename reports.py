import csv
from datetime import datetime
from config import FILE_NAME
import config
print(config.BUDGET)

def total_expense():

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)     

        for row in reader:
            total += float(row[3])

    print("\n--------------------------")
    print(f"Total Expense : ₹ {total}")
    print("--------------------------")



from budget import get_current_month_expense, get_remaining_budget
import config
config.BUDGET


def dashboard():

    total_records = 0
    highest = 0
    lowest = float("inf")

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            amount = float(row[3])

            total_records += 1

            if amount > highest:
                highest = amount

            if amount < lowest:
                lowest = amount

    if total_records == 0:
        lowest = 0
        average = 0
    else:
        average = get_current_month_expense() / total_records

    print("\n" + "=" * 55)
    print("              DASHBOARD")
    print("=" * 55)

    print(f"Total Records      : {total_records}")
    print(f"Current Budget     : ₹{config.BUDGET}")
    print(f"Current Expense    : ₹{get_current_month_expense()}")
    print(f"Remaining Budget   : ₹{get_remaining_budget()}")
    print(f"Highest Expense    : ₹{highest}")
    print(f"Lowest Expense     : ₹{lowest}")
    print(f"Average Expense    : ₹{average:.2f}")

    print("=" * 55)
