class Arithmetic:
    def __init__(self,Value1=0,Value2=0):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter the Value1: "))
        self.Value2 = float(input("Enter the Value2: "))
        print("Value of first number is:", self.Value1)
        print("Value of second number is:", self.Value2)

    def Addition(self):
        Ans = self.Value1 + self.Value2 
        print("Value of Add is:", Ans)
        
    def Substact(self):
        Ans = self.Value1 - self.Value2 
        print("Value of substact is:",Ans)
        
    def Division(self):
        Ans = self.Value1 / self.Value2
        print("Value of Division is:", Ans)        

    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        print("Value of Multiplication is:", Ans)


def main():
    obj1=Arithmetic()
    obj1.Accept()
    obj1.Addition()
    obj1.Substact()
    obj1.Multiplication()
    obj1.Division()


if __name__ == "__main__":
    main()