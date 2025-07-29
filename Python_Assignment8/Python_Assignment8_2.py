import threading
def evenfactor(n):
    sum =0
    for i in range(2,n,2):
        if n % i == 0:
            sum = sum + i
    print("Addition of evenfactors is:",sum)


def oddfactor(n):
    sum =0
    for i in range(1,n,2):
        if n % i == 0:
            sum = sum + i
    print("Addition of oddfactors is:",sum)
        
def main():
    print("Enter your number:")
    value = int(input())
    T1 = threading.Thread(target = evenfactor(value))
    T2 = threading.Thread(target = oddfactor(value))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    print("exit from main")
    
    
if __name__ == "__main__":
    main() 