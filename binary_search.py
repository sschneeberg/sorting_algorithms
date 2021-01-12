# needs to be non mutating to return index
# assume n and arr will contain same/similar types: strings + list of strings or int/float + list of ints/floats


# def binary_search(n, arr, start = 0, end = 0):
#     if end == 0: end = len(arr)
#     # not found if we have an empty list
#     if end - start == 0 :
#         return -1
#     if end - start == 1:
#         if arr[start] == n: return start 
#         return -1
#     else:
#         mid = 0
#         length = end - start
#         if length % 2 == 0: mid = (length // 2 ) + start
#         else: mid = (length - 1) // 2 + start
#     if arr[mid] < n:
#         return binary_search(n, arr, mid, end)
#     elif arr[mid] > n:
#         return binary_search(n, arr, start, mid)
#     elif arr[mid] == n: return mid

# print(binary_search(5, [1,3,4,5]))
# print(binary_search(85, [1,3,4,5,6,18,25,97,140,261]))
# print(binary_search('a', ['a', 'b', 'c']))

def binary_search(n, arr):
    if len(arr) == 0: return -1
    start, end = 0, len(arr)
    mid = 0
    while end - start > 1 :
        if (end-start) % 2 == 0: mid = (end-start) // 2 + start
        else: mid = (((end-start) - 1 ) // 2 )+ start
        if arr[mid] > n:
            # look in bottom half:
            end = mid
        elif arr[mid] < n:
            # look in top half:
            start = mid
        else: 
            # found it
            return mid
    if arr[start] == n : return start
    return -1

# print(binary_search(140, [1,3,4,5,6,18,25,97,140,261]))

def test_binary_search():
    test_list = [1, 2.25, 3, 5, 6, 7, 8, 9.5, 11]
    print('testing binary search')

    #should return and integer
    assert(type(binary_search(6, test_list)) == int)

    #should return a value less than the length of the list if the number is in the list
    assert(binary_search(6, test_list) < len(test_list))

    #should return -1 if the number is not in the list
    assert(binary_search(4, test_list) == -1) #bottom half
    assert(binary_search(9, test_list) == -1) #top half
    assert(binary_search(12, test_list) == -1) #above top value
    assert(binary_search(-3, test_list) == -1) #below top value
    assert(binary_search(6.5, test_list) == -1) #float

    #should return index if the number is in the list
    assert(binary_search(1, test_list) == test_list.index(0)) #first
    assert(binary_search(11, test_list) == test_list.index(11)) #last
    assert(binary_search(5, test_list) == test_list.index(5)) #lower half
    assert(binary_search(8, test_list) == test_list.index(8)) #top half
    assert(binary_search(2.25, test_list) == test_list.index(2.25)) #lower half float
    assert(binary_search(9.5, test_list) == test_list.index(9.5)) #upper half float

    print('success')

