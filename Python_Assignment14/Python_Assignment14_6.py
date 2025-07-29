class Calculator:

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
        
    def addition(self):
        ans = self.no1 + self.no2
        print("Addition:", ans)
        
    def multiplication(self):
        ans = self.no1 * self.no2
        print("Multiplication:", ans)  
        
    def subtraction(self):
        ans = self.no1 - self.no2
        print("Subtraction:", ans)
        
    def division(self):
        if self.no2 != 0:
            ans = self.no1 / self.no2
            print("Division:", ans)
        else:
            print("Division: Error! Cannot divide by zero.")
          
        
def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    obj1 = Calculator(num1, num2)
    obj1.addition()
    obj1.multiplication()
    obj1.subtraction()
    obj1.division()
    
if __name__ == "__main__":
    main()