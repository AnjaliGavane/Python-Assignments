def Power(x):
    result = lambda x : x ** 2
    return result(x)

def main():
    n=int(input("Enter your number:"))
    ans = Power(n)
    print("Number to the power is:",ans)
    
    
if __name__ == "__main__":
    main()    
