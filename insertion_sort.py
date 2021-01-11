def insertion_sort(arr):
    for i in range(len(arr)):
        position = i
        # even though the algorithm is deifned as move up, think about moving everything else down
        while position > 0 and arr[position-1] > arr[position]:
            arr[position], arr[position -1] = arr[position-1], arr[position]
            position -= 1


unsorted = [1,2,3,6,8,0,34,1,6,9,9,42]
insertion_sort(unsorted)


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

assert(is_sorted([1,2,3,4]) == True)
assert(is_sorted(unsorted) == True)