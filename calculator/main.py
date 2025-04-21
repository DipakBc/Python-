def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2 

def multiply(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

try:
    print("Welcome to the calculator made with python.")
    print("What operation ddo you want to perform.")
    print('''
            For addition press 1 
            For sutbtraction press 2
            For multipliction press 3 
            For division press 4
            To quit press 5 ''')
    user_input = int(input("Here is your input : "))

    try:

        number1 = int(input("Enter your first number : "))
        number2 = int(input("Enter your second number : "))

        try:
            if user_input == 1:
                print(f"The sum of {number1} and {number2} is {addition(number1, number2)}")

            if user_input == 2:
                print(f"The difference of {number1} and {number2} is {subtraction(number1, number2)}")

            if user_input == 3:
                print(f"The product of {number1} and {number2} is {multiply(number1, number2)}")

            if user_input == 4:
                print(f"The division of {number1} and {number2} is {division(number1, number2)}")

            if user_input == 5:
                print("Thanks for using :)")
                quit()

        except ValueError:
            print(ValueError)

    except ValueError:
        print(ValueError)
    
except Exception as e:
    print(e)