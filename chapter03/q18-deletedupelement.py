


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# /* 剑指Offer P122
#  * 题目：删除排序链表中的重复元素
#  * https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
#  */


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head














