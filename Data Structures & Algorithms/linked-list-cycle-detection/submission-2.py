# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Trying out the hint (Slow pointer and fast pointer)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # Dont actually use val for checking equivalence
                return True
            head = head.next
        return False
            





        # # Are all nodes distinct values? We will suppose they are (Incorrect assumption - case where head has not distinct values)
        # # How would we know whats a distinct value if we are unable to track based on value?
        # node1 = head
        # path = {} # We can have a dictionary where we store node1 as the key and node 2 as the connection etc.
        # while node1:
        #     node2 = node1.next 
        #     if node2:
        #         if node2.val in path:
        #             if node2.next in:
        #                 return True
        #         path[node1.val] = node2.val
        #     node1 = node2
        # return False

