class BankAccount:
     ROI = 10.5  # Rate of Interest
     
     def __init__(self, Name, Amount):
         self.Name = Name
         self.Amount = Amount
         
     def DisplayInfo(self):
         print("Accountholder Name: " + self.Name)
         print("Account Balance: " + str(self.Amount))
             
     def Deposit(self, add):
         self.Amount += add
         
     def Withdraw(self, sub):
         if sub > self.Amount:
             print("Insufficient balance!")
         else:
             self.Amount -= sub
         
     def CalculateInterest(self):
         # Calculate interest on current amount
         interest = self.Amount * BankAccount.ROI / 100
         self.Amount += interest
         print(f"Interest of {interest} added.")
                     
def main():
     obj1 = BankAccount("Megha", 200)
     obj1.Deposit(2000)
     obj1.Withdraw(100)
     obj1.CalculateInterest()
     obj1.DisplayInfo()
         
if __name__ == "__main__":
     main()