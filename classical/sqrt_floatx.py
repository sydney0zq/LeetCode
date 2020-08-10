import math

# https://blog.csdn.net/leviopku/article/details/82811478

# 二分法和牛顿法求根号是面试中的经典题，如果没提前接触过，经典题将成为经典难题


precision = 0.0000004

def sqrtx_dich(x):
    # assert x >= 1
    # But in this algorithm, x must be bigger than 1
    # because when x < 1, sqrt(x) is not between 0 and x, but sqrt(x) > x instead
    # therefore we reset the maxy to correct the borders
    miny = 0
    if x >= 1:
        maxy = x
    elif x >= 0 and x < 1:
        maxy = 1
    else:
        raise ValueError
    mid = x/2.0

    # formulation: when x-p< mid*mid < x+p, exit
    # ------------------------- maxy
    #
    # ------------------------- y + precision
    # ------------------------- y
    # ------------------------- y - precision
    # 
    # ------------------------- miny
    while mid*mid > x+precision or mid*mid < x-precision:
        mid = (miny+maxy)/2.0
        if mid*mid > x+precision:
            maxy = mid
        if mid*mid < x-precision:
            miny = mid

    return mid

















print (sqrtx_dich(0))

print (math.sqrt(5.0))



















