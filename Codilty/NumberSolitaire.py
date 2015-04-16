# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    MIN_VALUE = -1000000001
    N = len(A)
    max_val = [MIN_VALUE] * N
    max_val[0] = A[0]
    for x in xrange(N):
        for jump in xrange(6):
            y = x + jump + 1
            if (y >= N):
                break
            max_val[y] = max(max_val[x] + A[y], max_val[y])
    
    return max_val[N-1]