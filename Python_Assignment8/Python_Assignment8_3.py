import threading
def even(n):
    sum =0
    for i in n:
        if i % 2 == 0:
            sum = sum + i
    print("Addition of even list  is:",sum)


def odd(n):
    sum =0
    for i in n:
        if i % 2 != 0:
            sum = sum + i
    print("Addition of odd list  is:",sum)
    
        
def main():
    data=[]
    print("Enter your number:")
    value = int(input())
    
    print("Enter your list of  number:")
    for i in range(value):
        no = int(input())
        data.append(no)
    print("input data",data)    
    
    
    T1 = threading.Thread(target = even(data))
    T2 = threading.Thread(target = odd(data))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    print("exit from main")
    
    
if __name__ == "__main__":
    main() 