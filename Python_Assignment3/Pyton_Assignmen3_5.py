from MarvellousNum import ChkPrime

n = int(input("Enter number of elements: "))
numbers = []

print("Enter the elements:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

def ListPrime(numbers):
    return sum(num for num in numbers if ChkPrime(num))

print("Sum of prime numbers:", ListPrime(numbers))
