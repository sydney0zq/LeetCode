
## 01 Dynamic programming
# https://zhuanlan.zhihu.com/p/30959069

# Pseudo Code
# Input: n, w1, ..., wn, v1, ..., vn, C
# Maximum v1*x1 + ... + vn*xn, s.t. w1*x1 + ... +wn*xn <= C    xi {0, 1}

# 定义子问题 P(i, W) 为：在前 i 个物品中挑选总重量不超过 W 的物品，每种物品至多只能挑选1个，使得总价值最大；
# 这时的最优值记作 m(i, W)，其中 1<=i<=n ， 1<=W<=C 。

# Init boundaries, m 矩阵横向是W索引，纵向是物品id索引，顺序无关。m中值的意思表示在当前w下能获得的最大v
# for W in [0, C]:
#   m[0, W] = 0
# for i in [1, n]:
#   m[i, 0] = 0

# for i in [1, n]:
#   for w in [1, C]:
#       if wi > w:
#           m[i, w] = m[i-1, w]
#       else:
#           m[i, w] = max{m[i-1, w], vi+m[i-1, w-wi]}


import numpy as np

n = 4
C = 6
wm = [2, 2, 1, 2]       # 限制的时间, restricted by C
vm = [4, 35, 43, 10]    # Rewards

dp = np.zeros((n+1, C+1))

for i in range(1, n+1):
    wi = wm[i-1]
    vi = vm[i-1]
    for w in range(1, C+1):
        # print(wi, w)
        if wi > w:
            dp[i, w] = dp[i-1, w]
        else:
            # print ("----", dp[i-1, w], dp[i-1, w-wi])
            dp[i, w] = max(dp[i-1, w], dp[i-1, w-wi]+vi)

print (dp)
print (dp[n, C])
