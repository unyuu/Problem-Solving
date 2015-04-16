# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7

    # simplify the question:
    # provided that we can find the sums of elements closest and lower than sum(A) / 2
    # the sum of other parts of elements will be closest and greater than sum(A) / 2
    # which means the difference will be minimum
    N = len(A)
    M = 0
    for x in range(0, N):
        A[x] = abs(A[x])
        M = max(M, A[x])
    S = sum(A)
    count = [0] * (M+1)
    for x in range(0, N):
        count[A[x]] += 1

    dp = [-1] * (S+1)
    dp[0] = 0

    for x in range(1, M+1):
        if (count[x] > 0):
            for y in range(0, S):
                if dp[y] >= 0:
                    dp[y] = count[x]
                elif y >= x and dp[y-x] > 0:
                    dp[y] = dp[y-x] - 1

    result = S
    for x in range(0, S//2 + 1):
        if (dp[x] >= 0):
            result = min(result, S-2*x)
    return result