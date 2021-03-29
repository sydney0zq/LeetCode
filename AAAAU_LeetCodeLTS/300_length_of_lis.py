#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 qiang.zhou <qiang.zhou@Macbook>
#
# Distributed under terms of the MIT license.

"""
https://leetcode-cn.com/problems/longest-increasing-subsequence/
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:
        # init dp array
        if len(nums) == 0: return 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            n = nums[i]
            all_larger_dp = []
            for j in range(0, i):
                #print ("j", j)
                if n > nums[j]:
                    all_larger_dp.append(dp[j])
            #print (all_larger_dp)
            if len(all_larger_dp) != 0:
                dp[i] += max(all_larger_dp)

        return max(dp)


aa = [10,9,2,5,3,7,101,18]
#aa = [-2,-1]

print (Solution().lengthOfLIS(aa))


