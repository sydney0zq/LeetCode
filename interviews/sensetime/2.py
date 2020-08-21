def find_Good_pattern_ignore_G(s):
    # find o o d
    G = False
    o1 = False
    o2 = False
    d = False
    G_index = -1
    o1_index = -1
    o2_index = -1
    d_index = -1
    # print (s)
    for i, c in enumerate(s, 0):
        if c == "G" and G is False:
            G = True
            G_index = i
        
        if G is True:
            if c == "o" and o1 is False:
                o1 = True
                o1_index = i
            elif c == "o" and o1 is True:
                o2 = True
                o2_index = i
            elif c == "d" and o1 is True and o2 is True:
                d = True
                d_index = i
        
        if o1 and o2 and d and G:
            break
    
    if o1 and o2 and d:
        update_s = ""
        for i, c in enumerate(s):
            if i in (G_index, o1_index, o2_index, d_index):
                continue
            else:
                update_s += c
        return True, update_s
    else:
        return False, ""


def parse_s(s):
    ps = ""
    for c in s:
        if c in ['G', 'o', 'd']:
            ps += c
    return ps

import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    # s = "GooGGddGooGGooGoodddd"
    # s = "123 GoodoodGGoooddjfhjdGGooo3dkdggggGoood0123\n"
    s = parse_s(s)
    if len(s) == 0:
        print (0)
        exit()

    count = 0
    print (s)
    while True:
        flag, update_s = find_Good_pattern_ignore_G(s)
        # print (update_s, count)
        if flag is True:
            count += 1
            s = update_s
        else:
            break
    print (count)

    #print (count)
    #print(count_good_num(s))


