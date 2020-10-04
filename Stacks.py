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
