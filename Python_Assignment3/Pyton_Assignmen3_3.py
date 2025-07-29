def main(numbers):
    return min(numbers)

n = int(input("Enter number of elements: "))
numbers = []

print("Enter the elements:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

minimum = main(numbers)
print("minimum number from list : ",minimum)
