#bubble sort
def bubblesort(elements):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    # in asc order
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True

                # swapping data if the element is less than next element in the array
                elements[i], elements[i + 1] = elements[i + 1], elements[i] 
                print(elements)
    
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            return
 
elements = [5,4,3,2,1,6,7,8,9,10]
 
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array in Asc order is, ")
print(elements)
