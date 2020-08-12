# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/

from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # Sn = n*a1 + n*(n+1)*d/2
        # target = n * a1 + n*(n+1)/2, d=1
        # a1 = (target-(n*(n-1))/2)/n
        a1s = []
        l1s = []
        if target <= 2:
            return []
        res = []
        for n in range(2, target+1):
            a1 = (target-(n*(n-1))/2)/n
            if a1 <= 0:
                break
            # print (a1)
            # print (abs(a1-int(a1)) < 1e-3)
            if abs(a1-int(a1)) < 1e-5:
                start = int(a1)
                a1s.append(start)
                l1s.append(n)
                #res.append([start+i for i in range(0, n)])
        index = sorted([*range(0, len(a1s))], key=a1s.__getitem__)
        for i in index:
            i_res = [a1s[i]+x for x in range(0, l1s[i])]
            res.append(i_res)
        return res

res = Solution().findContinuousSequence(9)
print (res)


















