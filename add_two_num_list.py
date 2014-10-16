# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ret = ListNode(0)
        pt = ret
        while l1 or l2 or carry:
            add1 = 0; add2 = 0
            if l1:
                add1 = l1.val
                l1 = l1.next
            if l2:
                add2 = l2.val
                l2 = l2.next
            pt.next = ListNode((add1 + add2 + carry) % 10)
            carry = (add1 + add2 + carry) / 10
            pt = pt.next
        return ret.next
