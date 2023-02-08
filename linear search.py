#linear search
def lsearch(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]==key:
           return i
    return -1
       
        
arr=[5,4,3,2,1,6,7,8,9,10]

key=int(input("enter key: "))
h=lsearch(arr)
if h==-1:
    print("not found")
    
else:
    print("found element at index: ",h)