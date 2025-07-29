num = int(input("Enter a number to calculate factorial : "))

fact = 1

for i in range (1 , num + 1):
    fact = fact * i

print("factorial of given number is : ",fact)
