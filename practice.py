def word_break(str, dict):
    l = len(str)
    for i in range(l):
        first = str[0:i+1]
        if first in dict:
            second = str[i+1: l]
            if len(second) == 0 or second in dict or word_break(second, dict):
                return True
    return False

def all_palindromes(str):
    l = len(str)
    results = []
    def check_palindrome(j , k, str, p=''):
        while j >= 0 and k < l:
            if str[j] != str[k]:
                break
            p = str[j] + p + str[k]
            results.append(p)
            j -= 1
            k += 1

    for i in range(l):
        #even palindrome
        check_palindrome(i, i+1 ,str)
        #odd palindrome
        check_palindrome(i-1 ,i+1, str, str[i])
    return results

def longest_palindrome(str):
    n = len(str)
    maxCount = 1
    dp = [[0]*n for i in range(n)]
    for i in range(n):
        dp[0][i] = 1
    for i in range(n-1):
        if str[i] == str[i+1]:
            dp[1][i] = 2
            maxCount = 2
    for i in range(2, n):
        for j in range(n-i):
            if str[j] == str[j+i]:
                dp[i][j] = (dp[i-2][j+1] + 2) if dp[i-2][j+1] > 0 else 0
                if dp[i][j] > maxCount:
                    maxCount = dp[i][j]
    return maxCount

print(longest_palindrome('aabbaa'))

