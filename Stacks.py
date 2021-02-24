class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
            
    def pop(self):
        temp = None
        if self.head:
            temp = self.head.data
            self.head = self.head.next
        return temp

#https://www.hackerrank.com/challenges/balanced-brackets/problem
def isBalanced(s):
    mat = []
    def isPair(left, right):
        pairMap = {
        '{': '}',
        '[': ']',
        '(': ')'
        }
        if(left in pairMap and pairMap[left] == right):
            return True
        return False
    for i in range(0, len(s)):
        if len(mat) != 0:
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

#https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
class stacksQueue:
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()
        self.nextToCome = None
        
    def enqueue(self, x):
        if not self.stk1.head:
            self.nextToCome = x
        self.stk1.push(x)
        
    def dequeue(self):
        if not self.stk2.head:
            while True:
                temp = self.stk1.pop()
                if not temp:
                    break
                self.stk2.push(temp)
        self.stk2.pop()
    
    def getNext(self):
        return self.stk2.head.data if self.stk2.head else self.nextToCome