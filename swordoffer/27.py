#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""
https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursively
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        ## DFS, 深度优先搜索
        #if root is None:
        #    return None
        #if not root.left and not root.right:    # 判断是否是叶节点
        #    return root
        #root.left, root.right = root.right, root.left # 交换非叶节点的两个子节点
        #if root.left:
        #    self.mirrorTree(root.left)
        #if root.right:
        #    self.mirrorTree(root.right)
        #return root

        ## BFS, 广度优先搜索
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
        return root
    




