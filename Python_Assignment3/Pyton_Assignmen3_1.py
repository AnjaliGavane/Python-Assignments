def sum_of_elements(numbers):
    return sum(numbers)

n = int(input("Enter number of elements: "))
numbers = []

print("Enter the elements:")
for _ in range(n):
    num = int(input())
    numbers.append(num)

total = sum_of_elements(numbers)
print("Sum of elements:", total)
