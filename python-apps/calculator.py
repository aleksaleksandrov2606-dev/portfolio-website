result = 0

def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result
    
def division(num1, num2):
    result = num1 / num2
    return result

def simple_calc():
    
    first = int(input("Please put in the first number: "))
    more = "Yes"
    while more == "Yes":

        print(first)
        operator = input("Please choose the operator: ")
        second = int(input("Please put in the second number: "))

        if operator == "+":
            result = addition(first, second)
            print(result)
            first = result

        elif operator == "-":
            result = subtraction(first, second)
            print(result)
            first = result

        elif operator == "*":
            result = multiplication(first, second)
            print(result)
            first = result

        elif operator == "/":
            result = division(first, second)
            print(result)
            first = result
         
        more = input("Do you want to continue (Yes/No)?: ")
        
    else:
        print("Returning to home screen...")
        

def start_calc():

    while True:
        print("Welcome to the simple calculator!")
        user_choice = input("Do you want to start the calculator (Yes/No)?: ")

        if user_choice == "Yes":
            simple_calc()
        else:
            print("Closing the calculator...")
            break

start_calc()