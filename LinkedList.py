class Node:
    def __init__(self, dataval):
        self.data = dataval
        self.next = None

#https://binarysearch.com/problems/Kth-Last-Node-of-a-Linked-List
def kthLastNode(head, k):
    slow = head
    fast = head
    
    for i in range(k+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow.val