# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/




def get_cir_index(start, step, listlen):
    return (start+step) % listlen

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # brute force
        cir_list = [*range(0, n)]
        start_idx = 0
        while len(cir_list) != 1:
            start_idx = get_cir_index(start_idx, m-1, len(cir_list))
            del cir_list[start_idx]
        return cir_list[0]
        # conclude seems interesting
        # https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-by-lee/


ret = Solution().lastRemaining(10, 17)

print (ret)




# print (get_cir_index(3, 5, 2))



















