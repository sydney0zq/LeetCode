# https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/



class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        
        if head.val == val:
            return head.next
        
        savehead = head
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return savehead





