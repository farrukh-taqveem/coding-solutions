import math
def smallest_subarray_with_given_sum(s, arr):
  w_s = 0
  l = math.inf
  sm = 0
  for i in range(len(arr)):
    sm += arr[i]
    while (sm >= s):
      l = min(l, i - w_s + 1)
      sm -= arr[w_s]
      w_s += 1

  return l
  
  
def longest_substring_with_k_distinct(str, k):
  ws = 0
  l = 0
  d = {}
  for i in range(len(str)):
    if str[i] not in d:
      d[str[i]] = 0
    d[str[i]] += 1
    while(len(d) > k):
      d[str[ws]] -= 1
      if d[str[ws]] == 0:
        del d[str[ws]]
      ws += 1
    l = max(l, i - ws + 1)

  return l
  
  
def search_triplets(arr):
  arr.sort()
  triplets = []
  k = 0
  for i in range(len(arr)):
    if arr[i] == arr[i-1]:
      continue
    p = i + 1
    q = len(arr) - 1
    while (p < q):
      s = arr[i] + arr[p] + arr[q]
      if s == k:
        triplets.append([arr[i], arr[p], arr[q]])
        p += 1
        q -= 1
      elif s < k:
        p += 1
      else:
        q -= 1

  return triplets
  
  
#https://binarysearch.com/problems/Kth-Last-Node-of-a-Linked-List
def solve(self, node, k):
    slow = node
    fast = node
    
    for i in range(k+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow.val
  


def zero_sub_array(arr):
  d = {}
  sm = 0
  for i in range(len(arr)):
    d[str(sm)] = i
    sm += arr[i]
    if str(sm) in d:
      print(d[str(sm)], i)


arr = [11, 15, 16,17,1,0,9,5]
result = []
sum = 0
for i in range(len(arr)):
  sum += arr[i]

for i in range(len(arr)):
  print(sum - arr[i])
