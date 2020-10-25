#https://www.hackerrank.com/challenges/balanced-brackets/problem

def isBalanced(s):
    mat = []
    def isPair(left, right):
        temp = {
        '{': '}',
        '[': ']',
        '(': ')'
        }
        if left not in temp:
            return False
        if(temp[left] == right):
            return True
        return False

    n = len(s)
    for i in range(0, n):
        if len(mat) !=0:
            last = mat.pop()
            if not isPair(last, s[i]):
                mat.append(last)
                mat.append(s[i])
        else:
            mat.append(s[i])
    
    if len(mat) == 0:
        return "YES"
    return "NO"
    
#https://www.hackerrank.com/challenges/game-of-two-stacks/problem

def twoStacks(x, a, b):
    sum_a = sum_b = count = i = j = k = 0
    for item in a:
        if sum_a + item > x:
            break
        sum_a += item
        i +=1 
        
    for item in b:
        if sum_b + item > x:
            break
        sum_b += item
        j +=1
        
    count = i
    sm = sum_a
    
    while(i>=0 and k<j):
        sm += b[k]
        while(sm > x and i>0):
            i -=1
            sm -= a[i]
        k +=1
        if (i+k > count):
            count = i+k
            
    return count
