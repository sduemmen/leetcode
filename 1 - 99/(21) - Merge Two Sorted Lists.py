class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyhead = ListNode()
        ans = ListNode()
        dummyhead.next = ans

        if not l1 and not l2:
            return ans.next

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val: 
                    ans.val = l1.val
                    l1 = l1.next
                else:
                    ans.val = l2.val
                    l2 = l2.next
            elif l1:
                ans.val = l1.val
                l1 = l1.next
            elif l2:
                ans.val = l2.val
                l2 = l2.next
            if l1 or l2:
                ans.next = ListNode()
                ans = ans.next
        
        return dummyhead.next
