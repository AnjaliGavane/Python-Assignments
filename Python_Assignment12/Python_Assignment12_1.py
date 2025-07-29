class Demo :
     Value = 0 
     
     def __init__(self,no1,no2):
         self.no1 = no1
         self.no2  =no2
        
            
     def Fun(self):
         print("first variable:",self.no1)
          
         
             
     def Gun(self):
          print("second variable:",self.no2)
          
       
         
def main():
         obj1 =Demo(11,21)
         obj2 =Demo(51,101)
         obj1.Fun()
         obj1.Gun()
         obj2.Fun()
         obj2.Gun()
         
         
if __name__ == "__main__":
         main() 