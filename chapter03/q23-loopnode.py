# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# l1 = ListNode(-1)
# l2 = ListNode(-7)
# l3 = ListNode(7)
# l4 = ListNode(-4)
# l5 = ListNode(19)
# l6 = ListNode(6)
# l7 = ListNode(-9)
# l8 = ListNode(-5)
# l9 = ListNode(-2)
# l10 = ListNode(0)

# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
# l6.next = l7
# l7.next = l8
# l8.next = l9
# l9.next = l10
# l10.next = l8


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        # step 1, check there is loop or not
        # slowPtr = head
        # fastPtr = head
        # start_val = None
        # while True:
        #     if slowPtr.next is None or fastPtr.next is None or fastPtr.next.next is None:
        #         return None
        #     else:
        #         slowPtr = slowPtr.next
        #         fastPtr = fastPtr.next.next
        #         if slowPtr.val == fastPtr.val:
        #             start_val = slowPtr.val
        #             break
        # print ("start_val is {}".format(start_val))
        
        slowPtr = head
        fastPtr = head
        while (fastPtr != None and fastPtr.next != None):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if fastPtr == slowPtr:
                break;
        if fastPtr is None or fastPtr.next is None:
            return None

        # step 2, compute the loop length
        cnt = 1
        val = slowPtr.val
        slowPtr = slowPtr.next
        while (slowPtr.val != val):
            slowPtr = slowPtr.next
            cnt += 1
        loop_length = cnt
        print ("Loop length is {}...".format(loop_length))

        # step 3, set a slow&fast nodes to get the index
        slowPtr = head
        fastPtr = head

        for i in range(loop_length):
            fastPtr = fastPtr.next

        while True:
            if slowPtr.val == fastPtr.val:
                break
            else:
                fastPtr = fastPtr.next
                slowPtr = slowPtr.next
        print (fastPtr.val)
        return fastPtr

print (Solution().detectCycle(l1))
