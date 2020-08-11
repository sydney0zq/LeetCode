#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""
https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursively
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = maxDepth(root.left)
            right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1


# BFS

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        level = 0
        queue = [root]
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level





















