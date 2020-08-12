
# def find_max_K(classes):
#     some_0 = {}
#     some_1 = {}
#     max_some_0 = 0
#     max_some_1 = 0
#     for cls in classes:
#         if cls[0] not in some_0.keys():
#             some_0[cls[0]] = 1
#         else:
#             some_0[cls[0]] +=1 
#         if cls[1] not in some_1.keys():
#             some_1[cls[1]] = 1
#         else:
#             some_1[cls[1]] += 1
#         max_some_0 = max(max_some_0, some_0[cls[0]])
#         max_some_1 = max(max_some_1, some_1[cls[1]])
#     return  max(max_some_0, max_some_1)

def find_max_K(inputs):
    max_E = -1
    for s, e in inputs:
        if e >= max_E:
            max_E = e

    num_cls = len(inputs)
    oh_m = []
    for s, e in inputs:
        _oh_m = [0] * (s-1) + [1] * (e-(s-1)-1) + [0] * (max_E-e+1)
        oh_m.append(_oh_m)
    print (oh_m)
    max_cnt_list = []
    for c in range(max_E):
        cnt = 0
        for n in range(num_cls):
            if oh_m[n][c] == 1:
                cnt += 1
        max_cnt_list.append(cnt)
    print (max_cnt_list)
    max_cnt = max(max_cnt_list)
    return max_cnt
    
    
    
def find_max_K(inputs):
    max_E = -1
    for s, e in inputs:
        if e >= max_E:
            max_E = e

    num_cls = len(inputs)
    oh_m = []
    inplace_vec = [0] * max_E
    for s, e in inputs:
        _oh_m = [0] * (s-1) + [1] * (e-(s-1)-1) + [0] * (max_E-e+1)
        for ii, val in enumerate(_oh_m):
            if val == 1:
                inplace_vec[ii] += 1
    return max(inplace_vec)
        
    #     oh_m.append(_oh_m)
    # print (oh_m)
    # max_cnt_list = []
    # for c in range(max_E):
    #     cnt = 0
    #     for n in range(num_cls):
    #         if oh_m[n][c] == 1:
    #             cnt += 1
    #     max_cnt_list.append(cnt)
    # print (max_cnt_list)
    # max_cnt = max(max_cnt_list)
    # return max_cnt
    

def find_max_K(inputs):
    min_s = int(1e9)
    max_e = int(0)
    res = 0
    cur_cls = []
    remain_cls = inputs

    for cls in inputs:
        min_s = min(cls[0], min_s)
        max_e = max(cls[1], max_e)

    for i in range(min_s, max_e):
        # cur_cls_ = copy.deepcopy(cur_cls)
        cur_cls_ = cur_cls.copy()
        for cur in cur_cls:
            if cur[1] == i:
                cur_cls_.remove(cur)
        cur_cls = cur_cls_
        # remain_cls_ = copy.deepcopy(remain_cls)
        remain_cls_ = remain_cls.copy()
        for remain in remain_cls:
            if remain[0] == i:
                cur_cls.append(remain)
                remain_cls_.remove(remain)
        remain_cls = remain_cls_
    res = max(res, len(cur_cls))
    return res





#coding=utf-8

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    inputs = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        inputs.append(values)
    max_K = find_max_K(inputs)
    print (max_K)

    


