from art import logo

def add(n1,n2): return n1 + n2
def subtract(n1,n2): return n1 - n2
def multiply(n1,n2): return n1 * n2
def divide(n1,n2): return n1 / n2

operations = { '+': add, '-': subtract, '*': multiply, '/': divide }

def calculator():
    print(logo)
    for e in operations: print(e)
    num1 = float(input("what is first number: "))

    while True:  
        perfom = input("Type a math operation: ")
        num2 = float(input("what is next number: "))
        calculation = operations[perfom]
        answer = calculation(num1,num2)
        print(f"{num1} {perfom} {num2} = {answer}")
        print(f"Type 'y' to continue calculating with {answer},type n to exit or new to brand new calculation:")
        continue_calc = input("Type y/n/new: ")

        if continue_calc == 'y':
            num1 = answer
        elif continue_calc == 'n':
            print("\nGoodbye")
            return 
        elif continue_calc == 'new':
            calculator()
        else:
            print("Invalid response")
            break

calculator()
