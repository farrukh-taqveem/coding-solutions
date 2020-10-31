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
    
#https://binarysearch.com/problems/List-Min-Replacement
def solve(nums):
    if len(nums) == 0:
        return []
        
    m = nums[0]
    
    for i in range(1, len(nums)):
        temp = nums[i]
        nums[i] = m
        if(temp < m):
            m = temp
    nums[0] = 0
    return nums
    
#https://binarysearch.com/problems/Pigeonhole
def solve(self, ar):
    l = len(ar)
    a = sum(ar) - l*(l-1)/2
    return a
    
#https://binarysearch.com/problems/FizzBuzz
def solve(self, n):
    a = 3
    b = 5
    c = 15
    res = [str(i) for i in range(1,n+1)]
    l = len(res)
    for i in range(a-1, l, a):
        res[i] = 'Fizz'
    for i in range(b-1, l, b):
        res[i] = 'Buzz'
    for i in range(c-1, l, c):
        res[i] = 'FizzBuzz'
    return res
