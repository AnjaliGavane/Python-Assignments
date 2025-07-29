class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"


def main():
    
    product1 = Product("Laptop", 50000)
    product2 = Product("Phone", 50000)
    product3 = Product("Tablet", 30000)

    # Use __eq__ implicitly via ==
    if product1 == product2:
        print(f"{product1.name} and {product2.name} are equal in price.")
    else:
        print(f"{product1.name} and {product2.name} have different prices.")

    if product1 == product3:
        print(f"{product1.name} and {product3.name} are equal in price.")
    else:
        print(f"{product1.name} and {product3.name} have different prices.")
        
if __name__ == "__main__":
    main()              