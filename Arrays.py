#https://www.hackerrank.com/challenges/crush/problem

def arrayManipulation(n, queries):
    result = [0] * (n+2)
    for q in queries:
        result[q[0]-1] += q[2]
        result[q[1]] -= q[2]
    m = 0
    s = 0
    for i in range(0, n+1):
        s += result[i]
        if (s > m):
            m = s
    
    return m
