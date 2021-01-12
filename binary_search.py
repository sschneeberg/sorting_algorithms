# needs to be non mutating to return index
# assume n and arr will contain same/similar types: strings + list of strings or int/float + list of ints/floats


def binary_search(n, arr, start = 0, end = 0):
    if end == 0: end = len(arr)
    # not found if we have an empty list
    if end - start == 0 :
        return -1
    if end - start == 1:
        if arr[start] == n: return start 
        return -1
    else:
        mid = 0
        length = end - start
        if length % 2 == 0: mid = (length // 2 ) + start
        else: mid = (length - 1) // 2 + start
    if arr[mid] < n:
        return binary_search(n, arr, mid, end)
    elif arr[mid] > n:
        return binary_search(n, arr, start, mid)
    elif arr[mid] == n: return mid

print(binary_search(5, [1,3,4,5]))
print(binary_search(85, [1,3,4,5,6,18,25,97,140,261]))
print(binary_search('a', ['a', 'b', 'c']))

# def binary_search(n, arr):
#     if len(arr) == 0: return -1
#     start, end = 0, len(arr)
#     mid = 0
#     while end - start > 1 :
#         if (end-start) % 2 == 0: mid = (end-start) // 2 + start
#         else: mid = (((end-start) - 1 ) // 2 )+ start
#         if arr[mid] > n:
#             # look in bottom half:
#             end = mid
#         elif arr[mid] < n:
#             # look in top half:
#             start = mid
#         else: 
#             # found it
#             return mid
#     if arr[start] == n : return start
#     return -1

# print(binary_search(140, [1,3,4,5,6,18,25,97,140,261]))