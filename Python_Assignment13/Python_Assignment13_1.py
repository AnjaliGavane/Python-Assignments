class BookStore :
     noofbooks = 0 
     
     def __init__(self,Name,Author):
         self.Name = Name
         self.Author = Author
         noofbooks = 0
         BookStore.noofbooks += 1 
         
         
     def DisplayInfo(self):
         print("Book Name:"+self.Name)
         print("Book Author:"+self.Author) 
         print("no of books:",BookStore.noofbooks)
       
         
def main():
         obj1 =BookStore("Linux Operating System","Robert Love")
         obj1.DisplayInfo()
         obj2 =BookStore("C programming","Dennie Ritchie") 
         obj2.DisplayInfo()
         
         
if __name__ == "__main__":
         main() 