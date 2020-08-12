# https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/

from typing import List

class Solution:
    def twoSum(self, n: int) -> List[float]:
        # build dp array
        dp = []
        for _ in range(0, n+1):
            subdp = [0] * (6*n+1)
            dp.append(subdp)
        # init the first
        for i in range(1, 7):
            dp[1][i] = 1

        # increase
        for i in range(2, n+1):     # 2,3,4,....,n
            for j in range(i, 6*i+1):
                for k in range(1, 7):
                    if j-k >= 1:
                        dp[i][j] += dp[i-1][j-k]
        # print(dp)
        
        final_prob = []
        all_sum = sum(dp[n])
        for x in dp[n]:
            if x > 0:
                final_prob.append(x*1.0 / all_sum)
        return final_prob

print (Solution().twoSum(2))













