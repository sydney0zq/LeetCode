
all_perm = []
def permutations2(n):
    indices = list(range(1, n+1))
    # print(tuple(indices))
    global all_perm
    cycles = list(range(n, 0, -1))
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                # print(tuple(indices))
                all_perm.append(tuple(indices))
                break
        else:
            return

def count(all_perm, exs):
    remove_ids = []
    # print (all_perm)
    for i, x in enumerate(exs):
        for pi, item in enumerate(all_perm):
            if item[i] == x:
                remove_ids.append(pi)
    # print (remove_ids)
    return len(all_perm) - len(set(remove_ids))


import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    # 读取每一行
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    if n > 100:
        print (1000)
        exit(0)

    permutations2(n)
    ret_val = count(all_perm, values)
    print (ret_val)










# permutations2(3)
# print (all_perm)

# n = 3
# ex_a = [1, 2, 3]

# # all_perm = [1, 2, 3]
# # permutations(, 0, n)

# print (count(all_perm, ex_a))


