def main(numbers,target):
    print("frequency of number is :",numbers.count(target))

n = int(input("Enter number of elements: "))
numbers = []

print("Enter the elements:")

for _ in range(n):
    num = int(input())
    numbers.append(num)

target = int(input("Enter the number to search : "))

main(numbers, target)


