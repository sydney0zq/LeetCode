# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # Hash
        # hashdict = {}
        # for n in nums:
        #     if n not in hashdict.keys():
        #         hashdict[n] = 1
        #     else:
        #         return n
        # 本题难点在于原地操作
        # 因为所有数均为0-n-1之间，且长度为n，于是当不存在重复数字时，将其排序会使索引==值
        # 利用这一点我们将所有索引和值不相等的数进行交换，如果交换过程中发现重复，直接返回结果

        for i in range(len(nums)):
            while i != nums[i]:
                # 注意这里出错了，已经知道了i != nums[i]，应该考虑交换
                # 当i = nums[i]的时候，nums[nums[i]] == nums[i] = i
                if nums[i] == nums[nums[i]]:
                    # here we return i because
                    # i != nums[i] but i == nums[nums[i]]
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]

Solution().findRepeatNumber([0, 1, 2, 2])









