# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

