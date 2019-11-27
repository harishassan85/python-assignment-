'''
Make a calculator using Python with addition , subtraction , multiplication ,
division and power.
'''

num1 = int(input("Enter number 1: "))
oper = input("Enter Operator: ")
num2 = int(input("Enter number 2: "))

if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == '*':
    print(num1*num2)
elif oper == '/':
    print(num1 / num2)
elif oper == '^':
    print(num1**num2)    # ** is power sign in Python
else:
    print("Invalid operator")
