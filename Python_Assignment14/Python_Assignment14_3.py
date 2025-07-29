class Book:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        self.__price = price + 1

    def get_price(self):
        return self.__price

    def DisplayInfo(self):
        print("Book Price:", self.__price)


def main():
    obj1 = Book(130)
    obj1.set_price(150) 
    print("Updated Price:", obj1.get_price())
    obj1.DisplayInfo()


if __name__ == "__main__":
    main()