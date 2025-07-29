from functools import reduce

def prime(no1):
    primeno =True
    for i in range(2,no1):
        if no1 % i ==0:
            primeno =False
            
    if primeno:
        return True
    
def Mult (value1):
    ans = value1*2
    return ans

def max(no1,no2):
    if no1>no2:
        return no1
    else:
        return no2           

def main():
    data = []
    no1 = int(input("Enter the count:"))
    
    print("Enter the numbers from the list:")
    for i in range(no1):
        num = int(input())
        data.append(num)
    print("Input Data:",data) 
    
    FData = list(filter(prime,data))
    print("filter Data:",FData)
    
    
    Mdata = list(map(Mult,data))
    print("Map Data:",Mdata)
    
    
    Rdata = reduce(max,Mdata)
    print("Reduce output:",Rdata)
    
    
if __name__ == "__main__":
    main()  