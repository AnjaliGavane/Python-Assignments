from functools import reduce

def compare(no) :
   if( no>=70 and no<=90):
       return no
   
def Increase(no) :
   ans = no+10
   return ans

def Mult(no1,no2) :
   ans = no1+no2
   return ans



def main():
    data = [4,34,36,76,68,24,89,23,86,90,45,90]
    print("Input Data:",data) 
    
    FData = list(filter(compare,data))
    print("filter Data:",FData)
    
    
    Mdata = list(map(Increase,data))
    print("Map Data:",Mdata)
    
    
    Rdata = reduce(Mult,Mdata)
    print("Reduce output:",Rdata)
    
    
if __name__ == "__main__":
    main() 