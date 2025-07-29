def main(numbers):
    return max(numbers)

n = int(input("Enter number of elements: "))
numbers = []

print("Enter the elements:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

maximum = main(numbers)
print("maximum number from list : ",maximum)
