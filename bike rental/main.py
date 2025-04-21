# Bike Rental System.

class Bike_shop:
    def __init__(self, stock):
        self.stock = stock
    
    def avilable_stock(self):
        print(f"Total Bikes Currently avilable: {self.stock}")
    
    def rent_for_bike(self, quantity):

        if quantity <=0:
            print("Enter the positive value or greater then zero.")
        elif quantity > self.stock:
            print("Enter the value (less then stock).")
        else:
            self.stock = self.stock - quantity
            print(f"Total Price: {quantity * 100}")
            print(f"Total Bikes avilable: {self.stock}")
            
while True:
    bike_quantity = Bike_shop(100)
    user_choice = int(input('''
1 Display Stocks
2 Rent a Bike
3 Exit
Here is your input :  '''))
    
    if user_choice == 1:
        bike_quantity.avilable_stock()

    elif user_choice == 2:
        quantity = int(input("Enter the quantity : "))
        bike_quantity.rent_for_bike(quantity)
    else:
        break