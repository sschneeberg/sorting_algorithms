def quick_sort(n):
    if len(n) <= 1: return n
    pivot = n[-1]
    part_one, part_two = [], []
    for i in range(len(n)-1):
        if n[i] < pivot : part_one.append(n[i])
        else: part_two.append(n[i])
    return quick_sort(part_one) + [pivot] + quick_sort(part_two)

unsorted = [1,2,3,6,8,0,34,1,6,9,9,42]
sorted_arr = quick_sort(unsorted)

# print(quick_sort(['cat', 'dog', 'aardvark', 'armadillo', 'zebra', 'giraffe']))


def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

assert(is_sorted(sorted_arr) == True)