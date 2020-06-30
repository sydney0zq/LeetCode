# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3


# solution 1: stack
class Solution:
    def reversePrint(self, head):
        val_stack = []
        while head is not None:
            val_stack.append(head.val)
            head = head.next
        output_mem = []
        while len(val_stack) > 0:
            output_mem.append(val_stack.pop())
        return output_mem

# solution 2: recursive
class Solution:
    def reversePrint(self, head):
        if head is None:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]



# Iterate the ListNode
# l = l1
# while l is not None:
#     print (l.val)
#     l = l.next




