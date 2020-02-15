

def Calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2



result = Calc(int(input("Enter the first number")), int(input("Enter the secound number")), input("Enter the secound number"))
print(result)