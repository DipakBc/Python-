
import os

class Expense:
    def __init__(self, storeDate: str, description: str, amount: int):
        self.storeDate = storeDate
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"Date: {self.storeDate}, Description: {self.description}, Amount: {self.amount}"

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename
        self.expenses = self.loadExpenses()

    def addExpense(self, expense: Expense):
        self.expenses.append(expense)
        self.saveExpenses()
        print("Expense added successfully!")

    def viewExpenses(self):
        if not self.expenses:
            print("No expenses to show.")
        else:
            for idx, expense in enumerate(self.expenses, 1):
                print(f"{idx}. {expense}")

    def calculateTotal(self):
        if not self.expenses:
            print("No expenses to calculate.")
        else:
            total = sum(expense.amount for expense in self.expenses)
            print(f"Total Expenses: {total}")

    def saveExpenses(self):
        with open(self.filename, "w") as file:
            for expense in self.expenses:
                file.write(f"{expense.storeDate},{expense.description},{expense.amount}\n")

    def loadExpenses(self):
        if not os.path.exists(self.filename):
            return []

        expenses = []
        with open(self.filename, "r") as file:
            for line in file:
                date, description, amount = line.strip().split(",")
                expenses.append(Expense(date, description, int(amount)))
        return expenses

def main():
    tracker = ExpenseTracker()

    while True:
        try:
            userInput = int(input('''
    Choose an operation:
    1. Add expense
    2. View all expenses
    3. Calculate total expense
    4. Exit
    Your choice: '''))

            if userInput == 1:
                date = input("Enter the date (YYYY-MM-DD): ")
                description = input("Enter the description: ")
                try:
                    amount = int(input("Enter the amount: "))
                    expense = Expense(date, description, amount)
                    tracker.addExpense(expense)
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
            elif userInput == 2:
                print("\nExpense List:")
                tracker.viewExpenses()
            elif userInput == 3:
                tracker.calculateTotal()
            elif userInput == 4:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Please choose a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
