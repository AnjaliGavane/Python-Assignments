# arithmetic.py
def Add(a, b):
    return (a + b)

def Sub(a, b):
    return (a - b)

def Mult(a, b):
    return (a * b)

def Div(a, b):
    if (b != 0):
        return(a / b) 
    
    else:
        print("Division by zero error")

