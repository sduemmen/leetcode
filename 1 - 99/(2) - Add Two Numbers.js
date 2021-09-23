/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = (l1, l2) => {
    let head = new ListNode(), 
        result = head,
        first = l1,
        second = l2,
        carry = 0;
    
    while (first || second) {
        var sum = (first?.val ?? 0) + (second?.val ?? 0) + carry;

        result = result.next = new ListNode(sum % 10);
        carry = sum > 9 ? 1 : 0;

        first = first?.next;
        second = second?.next;
    }

    if (Boolean(carry)) result.next = new ListNode(1);
    
    return head.next;
};