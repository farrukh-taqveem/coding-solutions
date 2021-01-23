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
