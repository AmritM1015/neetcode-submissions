# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We check the head of both lists and whichever node is larger we add into the new list and call node.next
        # First Attempt
        # list3 = ListNode()
        # while (list1 and list2):
        #     if list1.val <= list2.val:
        #         list3.val = list1.val
        #         list1.next
        #     if list2.val < list1.val:
        #         list3.val = list2.val
        #         list2.next
        #     list3.next
        # return list3
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        # We check the head of both lists and whichever node is larger we add into the new list and call node.next
        dummy = list3 =  ListNode()
        while (list1 and list2):
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return list3.next
            
            