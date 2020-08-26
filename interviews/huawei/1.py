

## ac 了

def to_int32(num):
    return num & 0xffffffff

def int32_to_binstr(x):
    x = to_int32(x)
    return '{0:032b}'.format(x)

# step1
def shuffle_bits(num):
    new_num = ''
    for i in range(0, 31, 2):
        left, right = num[i], num[i+1]
        new_num += "{}{}".format(right, left)
    return new_num

def shift_bit(num_bits, x):
    left_bits = "0" * x
    length = len(num_bits)
    shift_num_bits = left_bits + num_bits[:length-x]
    return shift_num_bits, num_bits[length-x:]


def seqnoise(nums):
    # shuffle nums
    s_nums_bits = []
    n = len(nums)
    nums_bits = [int32_to_binstr(x) for x in nums]
    # print (nums_bits)

    for num in nums_bits:
        new_num = shuffle_bits(num)
        s_nums_bits.append(new_num)
    print(s_nums_bits)
    # generate src target pairs
    temp_bits = []
    shift_bits = []
    for x in s_nums_bits:
        _temp_bits, _shift_bits = shift_bit(x, 2)
        temp_bits.append(_temp_bits)
        shift_bits.append(_shift_bits)
    
    shift_bits = [shift_bits[-1]] + shift_bits[:-1]

    ret_bits = []
    for x, y in zip(temp_bits, shift_bits):
        _ret_bits = y + x[2:]
        ret_bits.append(_ret_bits)
    
    rets = [str(int(x, 2)) for x in ret_bits]
    rets = " ".join(rets)
    return rets


import sys
if __name__ == "__main__":
    # 读取第一行的n
    num_str = sys.stdin.readline().strip()
    nums = [int(x) for x in num_str.split(' ')]
    # nums = [1, 2, 3, 4, 5]
    # nums = [1, 2]
    print (seqnoise(nums))



