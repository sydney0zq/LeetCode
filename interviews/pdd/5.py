# 给一个排序好的字符串序列，如["aa", "abc", "", "bdc", "zf"]等
# 中间插入了一些空的字符串
# 现在给定一个字符串 s
# 找出s在这个序列中的index

# Q1: O(N)不接受
# Q2：如何处理空字符串的问题？


def shift2valid(l, mid):
    # left or right
    num = len(l)
    mid_in = mid
    while mid < num-1:
        if len(l[mid]) > 0:
            return mid
        else:
            mid = mid+1
    while mid >= 0:
        if len(l[mid]) > 0:
            return mid
        else:
            mid = mid-1
    assert False, "All invalid strings..."
    

def algo(l, s):
    left = 0
    right = len(l)
    mid = (left+right)//2
    
    while True:
        mid_s = l[mid]
        if len(mid_s) == 0:
            new_mid = shift2valid(l, mid)
            mid = new_mid
        mid_s = l[mid]
        # compare mid_s is bigger or smaller
        if s == mid_s:
            return mid
        elif s > mid_s:
            left = mid
            right = right
        elif s < mid_s:
            left = left
            right = mid
        mid = (left+right)//2


l = ["a", "bcc", "", "c", "", "d"]
print(algo(l, "d"))
