
import sys

def test(width_list, height_list):
    new_heigh_list = []
    for index, width in enumerate(width_list):
        if width > 1:
            while width > 0:
                new_heigh_list.append(height_list[index])
                width -= 1
        else:
            new_heigh_list.append(height_list[index])
    # print(new_heigh_list)
    return increase_stack(new_heigh_list)
def increase_stack(height_list):
    n = len(height_list)
    heights = height_list+[0]
    stack = [-1]
    max_area = 0
    for i in range(n+1):
        while heights[i]<heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h*w)
        stack.append(i)
    return max_area

import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    # s = "[-1],[2]"
    #s = "[1,1,1,1,2,1,1],[5,2,5,4,5,1,6]"
    # find the inter ],[
    try:
        index = s.index('],[')
        if index == 0: raise ValueError
        ws, hs = s[:index+1], s[index+2:]
        ws, hs = ws[1:-1], hs[1:-1]
        ws, hs = [int(x) for x in ws.split(',')], [int(x) for x in hs.split(',')]
        assert len(ws) == len(hs)
        # print (ws, hs)
        whs = ws+hs
        for x in whs:
            #print (x)
            if x <= 0:
                raise ValueError
        print (test(ws, hs))
    except:
        print (0)
