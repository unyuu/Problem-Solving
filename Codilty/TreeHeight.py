# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def findNextLevel(T, level):
    maxLevelLeft = level
    maxLevelRight = level
    if (T.l):
        maxLevelLeft = findNextLevel(T.l, level+1)
    if (T.r):
        maxLevelRight = findNextLevel(T.r, level+1)
    return max(maxLevelLeft, maxLevelRight)
    

def solution(T):
    # write your code in Python 2.7
    return findNextLevel(T, 0)