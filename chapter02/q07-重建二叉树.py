# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#    def __str__(self):
#        return str(self.value)

from typing import List
from base import BstNode

# 不会，难度有点大，注意前序和中序遍历
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/



# Solution: https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/er-cha-shu-de-qian-xu-bian-li-fen-zhi-si-xiang-by-/

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        self.preorder = preorder
        self.reverses = dict()

        assert len(preorder) == len(inorder)
        size = len(preorder)
        
        for i in range(size):
            self.reverses[inorder[i]] = i

        return self.__build_tree(0, size-1, 0, size-1)

    # 知道了 pre left&right 和 in left&right
    # 注意这个算法的核心是以preorder作为恢复的入口点，确定左右子树是通过inorder的长度来确定的
    # prel, prer, inl, inr指的都是以原始输入0元素作为坐标原点的索引，并不是右边界
    def __build_tree(self, prel, prer, inl, inr):
        if prel > prer or inl > inr:
            return None
        
        pivot = self.preorder[prel]
        root = BstNode(pivot)
        
        # for left, new args
        # prel+1, prel+1+pivot_inorder_index
        pivot_inorder_index = self.reverses[pivot]
        
        root.left = self.__build_tree(prel+1,
                                      prel+1+(pivot_inorder_index-inl)-1,       # 主要是为了算出left的宽度，利用pivot_inorder_index
                                      inl,
                                      pivot_inorder_index-1)

        root.right = self.__build_tree(prel+1+(pivot_inorder_index-inl)-1+1,    # 就是上面的prer再加一
                                       prer,
                                       pivot_inorder_index+1,
                                       inr)
        return root



preorder = [3,9,20,15,7]
inorder = [9,3, 15, 20, 7]


tree = Solution().buildTree(preorder, inorder)
tree.display()

