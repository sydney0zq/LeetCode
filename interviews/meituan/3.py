







def count_increase_seq_num(m, n, seq_x):
    tupleset = {}
    # 先满足第一个条件的个数有多少
    for i in range(n):      # left
        l = seq_x[i]
        for j in range(n):  # right
            r = seq_x[j]
            if l <= r and i != j:
                key = str(l) + "-" + str(r)
                if key in tupleset.keys():
                    tupleset[key] += 1
                else:
                    tupleset[key] = 1
    # print(tupleset)
    # 再满足第二个条件
    cnt = 0
    for key in tupleset.keys():
        l, r = [int(x) for x in key.split('-')]
        is_increase = True
        tmp = []
        for i in range(n):
            # print(seq_x[i])
            if seq_x[i] not in [*range(l, r+1)]:
                tmp.append(seq_x[i])
        for i in range(len(tmp)-1):
            if tmp[i] > tmp[i+1]:
                is_increase = False
                break
        if is_increase:
            cnt += tupleset[key]
    return cnt



def isvalid(nums):
    for idx, val in enumerate(nums):
        if idx == 0:
            continue
        if val < nums[idx - 1]:
            return False
    return True
 
def count_increase_seq_num_v2(m, n, nums):
    ret = 0
    r = m
    while r > 0:
        tmp1 = []
        for k in nums:
            if k > r:
               tmp1.append(k)
        if not isvalid(tmp1):
            break
        ll, rr = 1, r
        c = 0
        while ll <= rr:
            mid = (ll + rr) // 2
            tmp2 = []
            for k in nums:
                if (k < mid) or (k > r):
                    tmp2.append(k)
            if isvalid(tmp2):
                c = mid
                ll = mid + 1
            else:
                rr = mid - 1
        r -= 1
        ret += c
    print(ret)

import sys
if __name__ == "__main__":
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    # m, n = 5, 5
    # arr = [4, 1, 4, 1, 2]
    count_increase_seq_num_v2(m, n, arr)
    # print (cnt)

    # print (m, n, arr)









