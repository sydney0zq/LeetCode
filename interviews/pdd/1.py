




def func(K, N, steps):

    go_s = 0
    # 0 is paradox
    # -1 is backed
    # 1 is not reached
    stats = 0
    for s in steps:
        go_s += s
        if go_s == K:
            stats = 0
            break
        elif go_s > K:
            stats = -1
        else:
            continue
    if go_s < K:
        stats = 1

    # print (stats)

    if stats == 0:
        return "paradox"
    elif stats == -1:
        go_s = 0
        backed = 0
        for s in steps:
            tmp_go_s = go_s + s
            if tmp_go_s > K:
                go_s = K - (tmp_go_s-K)
                backed += 1
            elif tmp_go_s == K:
                return "paradox"
            elif tmp_go_s < K:
                go_s = tmp_go_s
        ret_string = "{} {}".format((K-go_s), backed)
        return ret_string
    elif stats == 1:
        ret_string = "{} 0".format(K-sum(steps))
        return ret_string


import sys
if __name__ == "__main__":
    # 读取第一行的n
    x = sys.stdin.readline().strip()
    m, n = [int(xi) for xi in x.split(' ')]
    steps = sys.stdin.readline().strip()
    # print (steps)
    steps = [int(s) for s in steps.split(' ')]

    # m = 10
    # n = 2
    # steps = [6, 3]

    # m = 10
    # n = 4
    # steps = [6, 3, 3, 3]


    # m = 6
    # n = 3
    # steps = [4, 2, 6]

    print(func(m, n, steps))
