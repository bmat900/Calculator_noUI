print('Welcome to the simple calculator app, no UI')

still_calculating = True

def calculator(num1, operator, num2):
    """Função que identifica o operador, e opera os dois numeros ingressados"""
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1/num2

while still_calculating == True:
    num1 = float(input("What's the first number?: "))
    print('+\n-\n*\n/')
    operator = input("Pick an operation: ")
    num2 = float(input("What's the second number?: "))
    result = round(calculator(num1, operator, num2), 1)
    print(f"{num1} {operator} {num2} = {result}")
    continu = input(
        f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or 'stop' to end: ")
    if continu == 'y':
        num1 = result
        print('+\n-\n*\n/')
        operator = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        result = round(calculator(num1, operator, num2), 2)
        print(f"{num1} {operator} {num2} = {result}")
        continu = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or 'stop' to end: ")
    if continu == 'stop':
        still_calculating = False
print('Thank you for using my first calculator! by bmat900')