class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name and Age of person is:", self.name, self.age)    
        
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  # Call the base class constructor
        self.subject = subject
        self.salary = salary
        
    def display(self):
        super().display()  # Optional: also show person info
        print("Subject and Salary is:", self.subject, self.salary)     
        
# Creating an object of Teacher
obj1 = Teacher("Priya", 34, "Maths", 34000)

# Displaying information
obj1.display()
              
                
                