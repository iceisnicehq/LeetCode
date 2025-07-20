# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l3 = head
        carry = False
        while True:
            l3.val = l3.val + l1.val + l2.val
            if l3.val > 9:
                l3.next = ListNode(1)
                l3.val = l3.val % 10
                l3 = l3.next
                carry = True
            else:
                carry = False
            if l1.next is None and l2.next is None:
                return head
            else:
                if not carry:
                    l3.next = ListNode()
                    l3 = l3.next
                if l1.next is not None:
                    l1 = l1.next
                else:
                    l1.val = 0
                if l2.next is not None:
                    l2 = l2.next
                else:
                    l2.val = 0

                            


        
