# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

# https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

from typing import List



# Two pointers
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1

        iseven = lambda x: (x % 2 == 0)
        isodd = lambda x: (x % 2 != 0)

        while left < right:
            # print (left, right)
            if iseven(nums[left]) and isodd(nums[right]):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            if isodd(nums[left]):
                left += 1
            if iseven(nums[right]):
                right -= 1
        return nums


# class Solution:
#     def exchange(self, nums: List[int]) -> List[int]:
#         odds = []
#         evens = []
#         for x in nums:
#             if x % 2 == 0:
#                 evens.append(x)
#             else:
#                 odds.append(x)
#         ret = odds + evens
#         return ret



print (Solution().exchange([1,2,3,4]))
















