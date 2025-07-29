from functools import reduce

def main():

    data = []

    print("enter number of elements : ")
    size = int(input())

    print("please enter numeric value : ")
    for i in range(size):
        num = int(input())
        data.append(i)

    
    
    fData = list(filter(lambda x : x % 2 == 0 ,data))
    print("Filtered data is : ",fData)

    mData = list(map(lambda x : x**2 ,fData))
    print("map output",mData)

    rData = reduce(lambda x,y : x+y , mData)
    print("reduced output is : ",rData)
    

if __name__ == "__main__":
        main()
        