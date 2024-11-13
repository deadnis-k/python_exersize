def calculator(a, b, operation):
    if operation== "*":
        print(a*b)
    elif operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    else:
        print(a//b)
        


num1= 20
num2= 30
oper= "*"
calculator(num1, num2, oper)
