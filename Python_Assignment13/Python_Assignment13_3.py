class Numbers:
    def __init__(self, num):
        self.num = num
         
    def Factors(self):
         factors = []
         for i in range(1, self.num):
             if self.num % i == 0:
                 factors.append(i)
         print(f"Factors of {self.num} (excluding itself): {factors}")
         return factors
     
    def SumFactors(self):
         factors = self.Factors()
         total = sum(factors)
         print(f"Sum of factors of {self.num}: {total}")
         return total
     
    def chkPrime(self):
         if self.num <= 1:
             print(f"{self.num} is not a prime number.")
             return False
         for i in range(2, int(self.num ** 0.5) + 1):
             if self.num % i == 0:
                 print(f"{self.num} is not a prime number.")
                 return False
         print(f"{self.num} is a prime number.")
         return True
     
    def chkPerfect(self):
         total = self.SumFactors()
         if total == self.num:
             print(f"{self.num} is a perfect number.")
             return True
         else:
             print(f"{self.num} is not a perfect number.")
             return False
 
def main():
     n = int(input("Enter a number: "))
     obj = Numbers(n)
     obj.Factors()
     obj.SumFactors()
     obj.chkPrime()
     obj.chkPerfect()
 
if __name__ == "__main__":
     main()