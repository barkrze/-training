# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        curr = result
        a = ListNode()
        b = ListNode()
        carry = 0
        a = l1
        b = l2
        
        while(a != None or b != None):
            sum = a.val + b.val + carry
            print(sum)
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if (a != None):
                a = a.next
            if (b != None):
                b = b.next
            
        if(carry > 0):
            curr.next = ListNode(carry)
        
        return result.next        
