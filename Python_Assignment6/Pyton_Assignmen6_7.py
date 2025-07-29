def find_largest():
    my_list = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        my_list.append(element)

    if not my_list:
        print("List is empty.")
        return None

    largest = my_list[0]
    for num in my_list:
        if num > largest:
            largest = num

    print("Largest number in the list is:", largest)
    return largest



def main():
    find_largest()
    
            
    
if __name__ == "__main__":
    main()     
    
    
                