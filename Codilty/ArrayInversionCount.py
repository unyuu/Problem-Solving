# you can use print for debugging purposes, e.g.
# print "this is a debug message"

count = 0

def merge(left, right):
    global count
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count = count + len(left) - i
    if i==len(left):
        merged.extend(right[j:])
    else:
        merged.extend(left[i:])
    return merged

def mergeSort(L):
    N = len(L)
    if (N > 1):
        left = mergeSort(L[0:N//2])
        right = mergeSort(L[N//2:])
        return merge(left, right)
    else:
        return L

def solution(A):
    # write your code in Python 2.7
    mergeSort(A)
    if count > 1000000000:
        return -1
    else:
        return count
    