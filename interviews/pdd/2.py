



# List all possibles of a touzi given a sequence

def hor_all_poss(l):
    a, b, c, d, e, f = l
    ret = [l]
    ret.append([a, b, d, c, f, e])
    ret.append([a, b, e, f, d, c])
    ret.append([a, b, f, e, c, d])
    return ret


def list_all_poss(l):
    a, b, c, d, e, f = l
    ret = [l]
    ret.append([b, a, c, d, f, e])
    ret.append([c, d, a, b, f, e])
    ret.append([d, c, a, b, e, f])
    ret.append([e, f, a, b, c, d])
    ret.append([f, e, a, b, d, c])
    all_poss = ret

    ext_ret = []
    for i_poss in all_poss:
        ext_poss = hor_all_poss(i_poss)
        ext_ret.extend(ext_poss)
    return ext_ret


def func(n, seqs):
    unqs = []
    if len(seqs) == 1:
        return 1, [1]
    if len(seqs) == 2:
        proc_seq = seqs[0]
        all_poss = list_all_poss(proc_seq)
        if seqs[1] in all_poss:
            return 1, [2]
        else:
            return 2, [1, 1]

    while len(seqs) >= 2:
        proc_seq = seqs[0]
        dup_cnt = 1
        all_poss = list_all_poss(proc_seq)
        # print (proc_seq)
        # print (len(seqs))
        to_del = []
        for i in range(1, len(seqs)):
            # import pdb
            # pdb.set_trace()
            if seqs[i] in all_poss:
                dup_cnt += 1
                to_del.append(i)
        # print (to_del)
        
        new_seq = []
        for i, x in enumerate(seqs):
            if not i in to_del:
                new_seq.append(x)
        seqs = new_seq
        # print (new_seq)

        unqs.append((proc_seq, dup_cnt))
        del seqs[0]
    
    if len(seqs) == 1:
        unqs.append((unqs[0], 1))
    
    vals = sorted([x[1] for x in unqs], reverse=True)
    # print (vals)
    return len(unqs), vals

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

    # print (inputs)
    # n = 2
    # inputs = [[1, 2, 3, 4, 5, 6], [1, 2, 6, 5, 3, 4]]
    # n = 5
    # inputs = [[1, 2, 3, 4, 5, 6], [1, 2, 6, 5, 3, 4], [1, 2, 3, 4, 6, 5], [6, 5, 1, 2, 4, 3], [4, 3, 1, 2, 5, 6]]

    # n = 10
    # inputs = [[2, 5, 1, 3, 4, 6], [5,4,3,2,1,6], [1,4,6,2,3,5], [1,5,6,3,4,2], [6,4,2,1,5,3], 
    # [3,6,4,5,2,1], [1,6,3,4,2,5], [5,1,4,2,6,3], [6,2,3,1,5,4], [5,3,6,1,4,2]]
    # print (n, len(inputs))
    num, vals = func(n, inputs)
    print (num)
    str_vals = ""
    for x in vals:
        str_vals += "{} ".format(x)
    print (str_vals[:-1])

    