

# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/



class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while (n > 0):
            to_add = n & 1
            n = n // 2
            res += to_add
        return res
