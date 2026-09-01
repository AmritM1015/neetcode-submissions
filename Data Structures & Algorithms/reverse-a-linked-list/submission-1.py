# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # We use recursion rather than looping
        # I dont really get why do it recursively if it takes the same time but more memory
        # if not head:
        #     return None
        
        # new_node = head

        # if head.next:
        #     new_node = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return new_node
        prev,curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        
        