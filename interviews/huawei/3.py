import sys



def guess(inputs):
    num = len(inputs)
    return inputs[num-1][0]




if __name__ == "__main__":
    # 读取第一行的n
    P = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    inputs = []
    for i in range(P):
        line = sys.stdin.readline().strip()
        inputs.append(line.split(' '))
    #nums = [int(x) for x in num_str.split(' ')]
    # nums = [1, 2, 3, 4, 5]
    # nums = [1, 2]
    # print (inputs)
    print (guess(inputs))