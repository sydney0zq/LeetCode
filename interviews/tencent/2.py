


import math

def ret_zero_cnt(A, B=1, C=-1):
    delta = B*B-4*A*C
    if delta > 0:
        return 2
    elif delta == 0:
        return 1
    else:
        return 0

def get_x1x2(A, B=1, C=-1):
    base = math.sqrt(B*B-4*A*B)
    x1 = (-B - base) / (2*A)
    x2 = (-B + base) / (2*A)
    return x1, x2

def in_interval(x, x1, x2):
    if x >= x1 and x <= x2:
        return True
    elif x <= x1 or x >= x2:
        return False

def Fx(A, B, x):
    return (1*A*x*x*x/3) + 0.5*x*x + B*x

def integral(abcd):
    A, B, C, D = abcd
    if C > D:
        C, D = D, C
    # get the zero points first

    zero_num = ret_zero_cnt(A=A, B=1, C=B)
    if zero_num == 0 or zero_num == 1:
        return abs(Fx(A, B, D) - Fx(A, B, C))
    elif zero_num == 2:
        x1, x2 = get_x1x2(A=A, B=1, C=B)
        x1_in = in_interval(x1, C, D)
        x2_in = in_interval(x2, C, D)
        # print (x1_in, x2_in)
        if x1_in and not x2_in:
            return abs(Fx(A, B, x1) - Fx(A, B, C)) + abs(Fx(A, B, D) - Fx(A, B, x1))
        elif not x1_in and x2_in:
            return abs(Fx(A, B, C) - Fx(A, B, x1)) + abs(Fx(A, B, D) - Fx(A, B, x2))
        elif x1_in and x2_in:
            return abs(Fx(A, B, x1) - Fx(A, B, C)) + abs(Fx(A, B, x2) - Fx(A, B, x1)) + abs(Fx(A, B, D) - Fx(A, B, x2))
        elif not x1_in and not x2_in:
            return abs(Fx(A, B, D) - Fx(A, B, C))



import sys
if __name__ == "__main__":
    # n A,B,C,D numbers
    n = int(sys.stdin.readline().strip())
    inputs = []
    for i in range(n):
       # 读取每一行
       line = sys.stdin.readline().strip()
       # 把每一行的数字分隔后转化成int列表
       values = list(map(float, line.split()))
       inputs.append(values)
    # inputs = [[-5, 5, 1, 2]]

    for abcd in inputs:
        print ("{:.06f}".format(integral(abcd)))






