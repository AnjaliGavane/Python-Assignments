# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

# Derived class
class Car(Vehicle):
    def start(self):
        print("Car is starting with keyless ignition...")  # Overriding base class method
        print("Additional checks: Seatbelt fastened, Fuel checked.")


def main():
    # Create objects
    v = Vehicle()
    c = Car()

    # Call start method on both
    print("Calling start on Vehicle object:")
    v.start()

    print("\nCalling start on Car object:")
    c.start()
    
    
if __name__ == "__main__":
    main()