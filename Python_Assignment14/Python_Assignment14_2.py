class Rectangle:
    
    def __init__(self, length=0,width=0):
        self.Area = 0
        self.Perimeter = 0

    def Accept(self):
        self.length = float(input("Enter the length: "))
        self.width = float(input("Enter the width: "))
        print("Value of length is:", self.length)
        print("Value of width is:", self.width)

    def CalculateArea(self):
        self.Area = self.length * self.width 
        print("Value of Area is:", self.Area)

    def CalculateCircumference(self):
        self.Perimeter = 2 * (self.length + self.width)
        print("Value of Perimeter is:", self.Perimeter)

    def DisplayInfo(self):
        print("Length and Width:", self.length,self.width)
        print("Area:", self.Area)
        print("Perimeter:", self.Perimeter)


def main():
    obj1 = Rectangle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.DisplayInfo()


if __name__ == "__main__":
    main()