#bubble sort

#for ascending order
def ascorder(element):
    n=len(element)
    swapped=False
    for i in range(n-1):
        for j in range(n-i-1):
            if element[j]>element[j+1]:
                swapped=True
                element[j], element[j + 1] = element[j + 1], element[j]
                print(element)
                
#for descending order
def desc(element):
    n=len(element)
    swapped=False
    for i in range(n-1):
        for j in range(n-i-1):
            if element[j]<element[j+1]:
                swapped=True
                element[j], element[j + 1] = element[j + 1], element[j]
                print(element)
                if not swapped:
                    return
#element=[5,4,3,2,1,6,7,8,9,10]
e=int(input("kuch bhi enter krdo")) 
for t in range(e):
    element=int(input("enter another element"))          
     