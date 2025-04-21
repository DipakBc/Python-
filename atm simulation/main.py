class Atm:
    
    bank_name = "Laxmi Sunrise"
    account_name = "Deepak Budha Chhetri"
    trans_id = 2580
    account_number = 123456

    def __init__(self):
        self.balance = 0  

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Rs{amount} is deposited into acc no:{self.account_number} named: {self.account_name} in {self.bank_name} bank successfully."
        else:
            return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount!"
        elif amount > self.balance: 
            return "Insufficient balance!"
        elif amount % 5 != 0: 
            return "Withdrawal amount must be in multiples of 5!"
        else:
            self.balance -= amount
            return f"Rs{amount} is withdrawn from acc no:{self.account_number} named: {self.account_name} in {self.bank_name} bank successfully."

    def account_detail(self):
        return f"Account name: {self.account_name}\nAccount number: {self.account_number}\nBank detail: {self.bank_name}"

    def account_status(self):
        return f"You have Rs{self.balance} currently in your account."

customer = Atm()

while True:
    try:
        customer_choice = int(input('''\nChoose the operations:
1 For Deposit.
2 For Withdraw.
3 To Check account detail.
4 To Check account status.
5 To Quit.
Here is your input: '''))

        if customer_choice == 1:
            amount = int(input("Enter amount to deposit: "))
            print(customer.deposit(amount))
            print(customer.account_status())

        elif customer_choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            print(customer.withdraw(amount))
            print(customer.account_status())

        elif customer_choice == 3:
            print(customer.account_detail())

        elif customer_choice == 4:
            print(customer.account_status())

        elif customer_choice == 5:
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid input! Please choose 1, 2, 3, 4, or 5.")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")
