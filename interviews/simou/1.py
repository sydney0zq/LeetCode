# 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

# 一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
 
# 请你返回从左上角走到右下角的最小 体力消耗值 。
# 输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
# 输出：2
# 解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
# 这条路径比路径 [1,2,2,2,5] 更优，因为另一条路劲差值最大值为 3 。

# 1 2 2
# 3 8 2
# 5 3 5

# dfs
arr = [
[1, 2, 2],
[3, 8, 2],
[4, 3, 5]
]
height = len(arr)
width = len(arr[0])

pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(arr, x, y, d, vis_arr):
    if x == width - 1 and y == height - 1:
        return True
    vis_arr[x][y] = 1       # label point is visited or not
    for i in range(4):
        new_x = x + pos[i][1]
        new_y = y + pos[i][0]
        # print (new)
        if 0 <= new_x < width and 0 <= new_y < height and vis_arr[new_x][new_y] != 1:
            # print (abs(arr[new_x][new_y]-arr[x][y]))
            if abs(arr[new_x][new_y]-arr[x][y]) <= d:
                if dfs(arr, new_x, new_y, d, vis_arr):
                    return True
    return False


def minpath(arr):
    max_d = 10000
    for i in range(0, max_d, 1):
        vis_arr = [[0] * width for i in range(height)]
        # print (i)
        if dfs(arr, 0, 0, i, vis_arr):
            print (i)
            break
    print ("done")
    

minpath(arr)




