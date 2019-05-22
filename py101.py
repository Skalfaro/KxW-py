num1 = float(input("enter num1: "))
op = input("enter operator: ")
num2 = float(input("enter num2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("no operator")