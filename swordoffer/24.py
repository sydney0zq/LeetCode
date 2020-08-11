#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""
https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pre = None
        cur = head
        # old nodelist:         1 -> 2 -> 3 -> NULL
        # new nodelist: NULL <- 1 <- 2 <- 3
        #               pre     cur
        # style 1
        #while cur.next is not None:
        #    _cur = cur.next
        #    cur.next = pre
        #    pre = cur
        #    cur = _cur
        #cur.next = pre
        #return cur
        # style 2
        while cur is not None:
            _cur = cur.next
            cur.next = pre
            pre = cur
            cur = _cur
        return pre






