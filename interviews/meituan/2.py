




def get_the_first_col(arr):
    res = []
    for seq in arr:
        if len(seq) > 0:
            res.append(seq[0])
    return res

def final_seq_v1(n, arr_vote):
    # update the table
    res = []
    while len(res) != n:
        first_col = get_the_first_col(arr_vote)
        
        # print ("first_col", first_col)
        for i in first_col:
            if i in res:
                continue
            else:
                res.append(i)
                # update table
                for ii, seq in enumerate(arr_vote):
                    for jj, sel in enumerate(seq):
                        if sel == i:
                            del arr_vote[ii][jj]
                break
    return res


def final_seq_v2(n, arr_vote):
    # 维护被用掉的业务
    used_ids = set()
    res = []

    for vote_seq in arr_vote:
        for vote_id in vote_seq:
            if vote_id in used_ids:
                continue
            else:
                used_ids.add(vote_id)
                res.append(vote_id)
                break
    return res





import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr_vote = []
    for i in range(n):
        row = sys.stdin.readline().strip()
        arr_vote.append([int(x) for x in row.split(' ')])
    # print (n, arr_vote)
    # n = 5
    # arr_vote = [[1, 5, 3, 4, 2], [2, 3, 5, 4, 1], [5, 4, 1, 2, 3], [1, 2, 5, 4, 3], [1, 4, 5, 2, 3]]
    x = get_the_first_col(arr_vote)
    res = final_seq_v2(n, arr_vote)
    out_str = ""
    for x in res:
        out_str += str(x) + " "
    print (out_str)





