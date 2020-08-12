



def func(inputs):
    n = len(inputs)
    input = []
    index = []
    for x, y in inputs:
        input.append(x)
        index.append(y-2)

    child_of_node = []
    for i in range(n):
        node_i = []
        for index_i in range(n):
            if index[index_i] == i and index[index_i] >= 0:
                node_i.append(index_i)
        child_of_node.append(node_i)
    
    max_output_old = input
    max_output =  input
    while True:
        for i in range(n):
            for point in child_of_node[i]:
                max_output[i] += max(0, max_output_old[point])
        if max_output == max_output_old:
            break
        max_output = max_output_old
    return max(max_output) % 1000000003





import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    inputs = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        inputs.append(values)
    val = func(inputs)
    print (val)
