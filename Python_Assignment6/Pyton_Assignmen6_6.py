def patterns(rows):
    for i in range(1, rows + 1):  # Outer loop for rows
        for j in range(1, i + 1):  # Inner loop for columns
            print("*", end=" ")   # Print star
        print()        
    

def main():
    rows = int(input("Enter the row size for the pattern: "))
    patterns(rows)
        
if __name__ == "__main__":
    main() 

    