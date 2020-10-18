#https://binarysearch.com/problems/Sum-of-the-digits

def rec (num, d=0):
    if num == 0:
        return d
    s = rec(num//10, num%10)
    return s+d
