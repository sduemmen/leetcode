# 72 ms
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        result = temp
        p = l1
        q = l2
        carry = 0
        while not (p is None and q is None):
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = x + y + carry
            carry = sum//10
            result.next = ListNode(sum % 10)
            result = result.next    
            p = p.next if p is not None else None
            q = q.next if q is not None else None
        if carry:
            result.next = ListNode(carry)
        return temp.next

def createListNodefromList(l: list):
    tempNode = ListNode(0)
    node = tempNode
    for element in l:
        node.next = ListNode(element)
        node = node.next
    return tempNode.next

def printListNode(listnode: ListNode):
    result = []
    while listnode:
        result.append(listnode.val)
        listnode = listnode.next
    print(result)

a = createListNodefromList([2,4,3])
b = createListNodefromList([5,6,4])
c = createListNodefromList([0])
d = createListNodefromList([0])
e = createListNodefromList([9,9,9,9,9,9,9])
f = createListNodefromList([9,9,9,9])

printListNode(Solution.addTwoNumbers(Solution, a, b))
printListNode(Solution.addTwoNumbers(Solution, c, d))
printListNode(Solution.addTwoNumbers(Solution, e, f))
