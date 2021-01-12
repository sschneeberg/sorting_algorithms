def merge(n,m):
    merged_arr = []
    while len(n) > 0 and len(m) > 0:
        if n[0] > m[0]: 
            merged_arr.append(m[0])
            m = m[1:]
        else: 
            merged_arr.append(n[0])
            n = n[1:]
    # deal with unequal lengths
    if len(n) > 0 : merged_arr = merged_arr + n
    elif len(m) > 0: merged_arr = merged_arr + m
    return merged_arr

# assuming an array of integers, but technically this works with strings
def merge_sort(n):
    # empty and single element (base case) arrays are sorted
    if len(n) <= 1: return n
    else: 
        if len(n) % 2 == 0:
            ind = len(n) // 2 
            return merge(merge_sort(n[0:ind]), merge_sort(n[ind:]))
        else: 
            ind = (len(n)-1) // 2
            return merge(merge_sort(n[0:ind]), merge_sort(n[ind:]))

unsorted = [1,2,3,6,8,0,34,1,6,9,9,42]
sorted_arr = merge_sort(unsorted)

# print(merge_sort(['cat', 'dog', 'aardvark', 'armadillo', 'zebra', 'giraffe']))


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

assert(is_sorted(sorted_arr) == True)