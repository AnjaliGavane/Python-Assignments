class BankAccount:
    
    def __init__(self,Account_number,name,balance):
        self.Account_number = Account_number
        self.name = name
        self.balance = balance
        
        
    def deposit(self):
        amount = int(input("Enter amount to deposit"))
        self.balance = self.balance + amount 
        print("Balance after deposit is :",self.balance) 
        
    def withdraw(self):
        amount = int(input("Enter amount to withdraw"))
        self.balance = self.balance - amount 
        print("Balance after withraw is :",self.balance) 
        
    def display_info(self):
        print("Account number:", self.Account_number)
        print("Balance:", self.balance) 
        
        
def main():
    obj1 = BankAccount(123456,"Rama",189)
    obj1.deposit()
    obj1.withdraw()
    obj1.display_info()
    
if __name__ == "__main__":
    main()    
                
        
          