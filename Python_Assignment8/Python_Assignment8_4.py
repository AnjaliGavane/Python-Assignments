import threading
def small(n):
    ans =0
    for i in n:
        if (i >= 'a' and  i<'z'):
            ans = ans + 1
    print("Number of small characters:",ans)
    print("Thread ID is :",threading.get_ident())        
    print("thread name is:",threading.current_thread().name)


def Capital(n):
    ans =0
    for i in n:
        if (i >= 'A' and  i<'Z'):
            ans = ans + 1
    print("Number of upper characters:",ans)
    print("Thread ID is :",threading.get_ident())        
    print("thread name is:",threading.current_thread().name)
    
def digit(n):
    ans =0
    for i in n:
        if (i.isdigit()):
            ans = ans + 1
    print("Number of digits:",ans)
    print("Thread ID is :",threading.get_ident())        
    print("thread name is:",threading.current_thread().name)
    
    print()    
   
    
        
def main():
    print("Enter your string:")
    value = input()
       
    
    T1 = threading.Thread(target = small(value))
    T2 = threading.Thread(target = Capital(value))
    T3 = threading.Thread(target = digit(value))
    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()
    
    
if __name__ == "__main__":
    main() 