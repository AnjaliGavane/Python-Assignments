from functools import reduce

def main():

    data = []

    print("enter number of elements : ")
    size = int(input())

    print("please enter numeric value : ")
    for i in range(size):
        data.append(i)

    
    
    fData = list(filter(lambda x : 70 <= x <= 90 ,data))
    print("Filtered data is : ",fData)

    mData = list(map(lambda x : x + 10 ,fData))
    print("map output",mData)

    rData = reduce(lambda x,y : x*y , mData)
    print("reduced output is : ",rData)


    
    if __name__ == "__main__":
        main()
        