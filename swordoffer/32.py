# https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        # BFS
        if root is None:
            return ret
        queue = [root]
        while len(queue) > 0:
            level_elem = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level_elem.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(level_elem)
        return ret


                




















