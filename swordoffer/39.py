# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort solution
        # nums_sorted = sorted(nums)
        # return nums_sorted[len(nums)//2]

        # Moree vote, can only applied to the number count > len(nums)//2
        vote = nums[0]
        count = 1
        for n in nums[1:]:
            # print (vote)
            if count == 0:
                vote = n
                count = 1       # Note this assignment
            else:
                if vote == n:
                    count += 1
                else:
                    count -= 1
        return vote
print (Solution().majorityElement([0, 0, 0, 0, 2, 1]))













