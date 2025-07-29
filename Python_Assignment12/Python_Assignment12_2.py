class Circle:
    pi = 3.14

    def __init__(self, radius=0):
        self.radius = radius
        self.Area = 0
        self.Circumference = 0

    def Accept(self):
        self.radius = float(input("Enter the radius: "))
        print("Value of radius is:", self.radius)

    def CalculateArea(self):
        self.Area = self.radius * self.radius * Circle.pi
        print("Value of Area is:", self.Area)

    def CalculateCircumference(self):
        self.Circumference = 2 * self.radius * Circle.pi
        print("Value of Circumference is:", self.Circumference)

    def DisplayInfo(self):
        print("Radius:", self.radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)


def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.DisplayInfo()


if __name__ == "__main__":
    main()