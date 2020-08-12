# https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Solved by myself
        # 1. find the length difference of ListNodeA and ListNodeB
        # 2. let the longer one goes difference steps
        # 3. sync steps and then check there 
        node1, node2 = headA, headB

        lenA = 0
        while node1 is not None:
            lenA += 1
            node1 = node1.next
        lenB = 0
        while node2 is not None:
            lenB += 1
            node2 = node2.next
        
        node1, node2 = headA, headB

        if lenA > lenB:
            lenD = lenA-lenB
        elif lenA < lenB:
            lenD = lenB-lenA
            node1, node2 = headB, headA
        else:
            lenD = 0

        for i in range(lenD):
            node1 = node1.next

        while True:
            if node1 == node2 or node1 is None or node2 is None:
                break
            else:
                node1 = node1.next
                node2 = node2.next

        if node1 == node2:
            return node1
        else:
            return None
