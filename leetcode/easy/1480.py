# q1480: https://leetcode-cn.com/problems/running-sum-of-1d-array/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        dy_sum = []
        acc_sum = 0
        for x in nums:
            acc_sum += x
            dy_sum.append(acc_sum)
        return dy_sum



x = Solution().runningSum([1, 2, 3, 4])
print (x)


        



























