#Longest Common Substring (Educative.io)
def LCStr(str1, str2):
	n = len(str1)
	m = len(str2)
	store = [ [0] * (m+1) for i in range(n+1)]

	l = 0
	for i in range(1, n + 1):
		for j in range(1, m + 1):
    		if(str1[i-1] == str2[j-1]):
        	store[i][j] = store[i-1][j-1] + 1
        	l = max(l, store[i][j])

	return l

def longest_valid_paranthesis(str):
    l = len(str)
    dp = [0]*len(str)
    for i in range(l):
        if str[i] == '(':
            dp[i] = 0
        elif str[i-1] == '(':
            dp[i] = dp[i-2] + 2
        elif str[i - dp[i-1] - 1] == '(':
            dp[i] = dp[i-1] + 2 + dp[i - (dp[i-1] + 2)]
    return dp[l - 1]