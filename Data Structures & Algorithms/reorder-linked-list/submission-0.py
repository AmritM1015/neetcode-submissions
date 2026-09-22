# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        i,j = 0, len(nodes)-1

        while i < j:
            nodes[i].next = nodes[j]
            i+=1
            if i>=j:
                break
            nodes[j].next = nodes[i]
            j -=1
        
        nodes[i].next = None

"""
Reorder linked list.

You are given the head of a singly linked list. The positions of a linked list of length 7, for example, can initially be represented as 0123456. Reorder the nodes of the linked list to be in the following order: 0615, 243.

In the general case, label the nodes by their original zero-based position from 0 to n - 1. We labeled the nodes, and after reordering, those original positions appear in this order: 0, n - 1, 1, n - 2, 2, n - 3, and so on. These numbers represent node positions, not values stored in the nodes. You may not modify the values in the list nodes, but instead you must reorder the nodes themselves.

I think that there has to be some kind of formula here that we are working with. 
There's clearly some mathematical trick that we have to use here. I'm not exactly sure, so let me look at the hint real quick, or I'll look at the topics. Here it's listed:
- linked list
- two pointers
- stack
- recursion
We can use a stack (that's what the argument seems to be), or we can use two pointers, or recursion. All right, I guess I'll look at the solution.
The hints or the prerequisites here say linked list and fast and slow pointers, so we should have some fast pointer that recurses through the list one way, and then a slow pointer. Let's see. I'll look at the solution.
There's first the brute force, where we store all the nodes in an array. Once we store them, we access the nodes from start and end using two pointers, and we alternately link nodes back and forth, I guess. For example, 0 will be at the beginning, and 1 will be at the last index. I think, really, 0 to n/2 - 1 will be the front weight, front direction, and then after that it comes backwards all the way to n - 1, the second-to-last index.
Of course, there's the end solution where we're appending the nodes. All the nodes are just appended to the list, as he said. Then we have an i and j pointer, left and right pointer, where we keep doing `node[i].next = node[j]`. Once i becomes greater than j, then we go `node[j].next = node[i]`, then j - 1. Not exactly sure why this works. I'll copy-paste this and see how it works.all right, we have `if not head, we return`, so I think this is a recursive method, or no, this is the safeguard in case the node `head` itself is `null`. Next, `i = 0`, `j = len(nodes) - 1`.
What I'm not so sure on is why the right pointer makes that work: `nodes[i].next`. I think I understand how it kind of works. We alternate between `i` and `j`:
- `i` at the start of the array
- `j` at the end of the array
- `i` at the next index
- `j` at the next index
`j` decrements while `i` increments. I can see how that would work, and then eventually we get to the point where `i >= j`, and then we just break. That'll be specifically at the midpoint of the array, or it would be when `i >` the midpoint of the array. We break there because we know that at that point there can be no elements from `j` after that that haven't been covered. I understand how that works now.

"""