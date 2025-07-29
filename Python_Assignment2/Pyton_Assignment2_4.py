
num = int(input("Enter a positive integer: "))

sum_factors = 0

for i in range(1, num):
    if num % i == 0:
        sum_factors += i  

print("Sum of factors:", sum_factors)
