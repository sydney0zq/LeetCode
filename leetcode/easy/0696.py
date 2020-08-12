# https://leetcode-cn.com/problems/count-binary-substrings/


def find_common_length(s):
    templ = s[0]
    count = 1
    for c in s[1:]:
        if templ == c:
            count += 1
        else:
            break
    return count

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0: return 0
        pn_count = []

        while True:
            v = find_common_length(s)
            pn_count.append(v)
            s = s[v:]
            if len(s) == 0:
                break
        
        res = 0
        for u, v in zip(pn_count, pn_count[1:]):
            res += min(u, v)
        return res


print (Solution().countBinarySubstrings("1"))
#print (find_common_length("00110011"))







