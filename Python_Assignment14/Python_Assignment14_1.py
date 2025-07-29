class Employee :
     
    def __init__(self,name,id,salary):
         self.name = name
         self.id  = id
         self.salary = salary
         
    def DisplayInfo(self):
         print("Employee Name:"+self.name)
         print("Employee id:",self.id) 
         print("Employee Salary:",self.salary)
                   
         
def main():
         obj1 = Employee("Rohit" ,123,34000)
         obj1.DisplayInfo()
         
         
if __name__ == "__main__":
         main() 