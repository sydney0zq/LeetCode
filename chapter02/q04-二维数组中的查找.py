# 剑指offer P63

# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        # px, py是用来和target比较大小的坐标，注意初始化的val是右上角
        px, py = cols-1, 0
        while True:
            # print (py, px)
            right_upper_val = matrix[py][px]
            if right_upper_val == target:
                return True
            elif right_upper_val > target:
                # 注意这两个if判断，非常容易错，主要是对于只有一列的边界情况，如果不else的话会导致死循环
                # 这两句的意思是如果减到只有1列的话，并且右上角的值还大于target，那么必然return False
                if px > 0: px -= 1
                else: return False
            elif right_upper_val < target:
                # 和上面的是对称的情况，很容易出错
                if py < rows-1: py += 1
                else: return False

            # 这两句用来判定左下角的值的是否和target相同的，也没有必要了，被各自的if判断处理了
            # if px == 0 and py == rows-1 and matrix[py][px] != target:
            #     return False

# m = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# print (Solution().findNumberIn2DArray(m, 5))
# print (Solution().findNumberIn2DArray(m, 20))

# m = [[1,1]]

# print (Solution().findNumberIn2DArray(m, 2))

#m = [[3,5,9,9,14],[7,8,11,15,15],[8,10,16,16,17]]
#print (Solution().findNumberIn2DArray(m, 12))
m=[[-1],[-1]]
print (Solution().findNumberIn2DArray(m, -2))