from functools import reduce

def is_prime(n) :
    
    if n < 2:
        return False
   
    for i in range(2, n):
        if n % i == 0:
           return False
            
        return True

def main():

    data = []

    print("enter number of elements : ")
    size = int(input())

    print("please enter numeric value : ")
    for i in range(size):
        num = int(input())
        data.append(num)

    fdata = list(filter(is_prime, data))

    mdata = list(map(lambda x: x * 2, fdata))

    rdata = reduce(lambda x, y: max(x, y), mdata)

    print("Input List =", data) 
    print("List after filter =", fdata)
    print("List after map =",mdata)
    print("Output of reduce =", rdata)


if __name__ == "__main__":
    main()
        

