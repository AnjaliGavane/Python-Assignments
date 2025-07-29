# main.py
import arithmatic

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", arithmatic.Add(a, b))
    print("Subtraction:", arithmatic.Sub(a, b))
    print("Multiplication:", arithmatic.Mult(a, b))
    print("Division:", arithmatic.Div(a, b))

main()
