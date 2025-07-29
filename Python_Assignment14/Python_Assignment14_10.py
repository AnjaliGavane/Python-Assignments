class Employee:
    def __init__(self, name, department, salary):
        self.name = name              # Public
        self._department = department # Protected
        self.__salary = salary        # Private

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount.")
            
def main():
    emp = Employee("Rohit", "Finance", 50000)
    print("Public Access:")
    print(emp.name)
    print("\nProtected Access:")
    print(emp._department) 
    print("\nPrivate Access:")
    try:
        print(emp.__salary) 
    except AttributeError as e:
        print("Cannot access private attribute directly:", e)
    print("\nAccessing private attribute using method:")
    print(emp.get_salary())
    emp.set_salary(55000)
    print("Updated salary:", emp.get_salary())
    
    
if __name__ == "__main__":
    main()       