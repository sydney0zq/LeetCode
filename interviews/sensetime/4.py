

import numpy as np

l = [1, 2, 3, 3, 4, 5, 7, 8, 10]

l1 = [1,2,3,4]
l2 = [3,5,7,8,10]

print (np.median(l))

num1 = len(l1)
num2 = len(l2)

start1 = num1 // 2
start2 = num2 // 2

# def bound1(x):
#     return min(max(0, x), num1-1)
# def bound2(x):
#     return min(max(0, x), num2-1)


if l1[start1] == l2[start2]:
    print (l1[start1])
    exit()
else:
    if l1[start1] < l2[start2]:
        while True:
            l1_val = l1[start1]
            l2_val = l2[start2]
            start1 += 1
            # start1 = bound1(start1)
            if start1 == num1:
                start1 = 0
                l1 = l2
            if l1[start1] >= l2_val:
                print (l2_val)
                exit()
            start2 -= 1
            if start2 == -1:
                start2 = num1-1
                l2 = l1
            if l1_val >= l2[start2]:
                print (l1_val)
                exit()
    else:
        # while True:
        #     start1 -= 1
        #     start1 = bound1(start1)
        #     start2 += 1
        #     start2 = bound2(start2)
        #     if l1[start1] == l2[start2]:
        #         print(l1[start1])
        #         exit() 

            
            




















