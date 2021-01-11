def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

unsorted = [1,2,3,6,8,0,34,1,6,9,9,42]
bubble_sort(unsorted)

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

assert(is_sorted([1,2,3,4]) == True)
assert(is_sorted(unsorted) == True)