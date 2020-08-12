# Given a list with some int elements, get max XOR of two elements
# e.g. List [2, 5, 6, 8]
# max XOR is 14

# Brute force
def find_max_xor(l):
    vals = []
    for x in l:
        for y in l:
            if y != x:          # Actually when x == y, x ^ y = 0
                val = x^y
                vals.append(val)
    return max(vals)

##################################################################

# Bitwise comparing version 1

# Support 32 bit now, acutally it can be replaced by bit moving
# Here we keep it for readability
def int2binstr(x):
    return '{0:032b}'.format(x)

def find_max_xor2(l):
    # l = list(set(l))              # Uncomment when duplicated elements exist

    # Find highest bit == 1 index
    l_bs = [int2binstr(x) for x in l]
    first1_ind = 0
    for i in range(0, 32):
        first1_sum = 0
        for x in l_bs:
            if x[i] == "1":
                first1_sum += 1
        if first1_sum > 0 and first1_sum != len(l_bs):
            first1_ind = i
            break

    # Split highest bit == 1 and highest bit == 0
    g1, g0 = [], []
    for x in l_bs:
        if x[first1_ind] == "1":
            g1.append(x)
        else:
            g0.append(x)
    
    # Form highest bit 1&0 pairs
    xor_pairs = [(x, y) for x in g1 for y in g0]
    
    # Compare from highest bit to lowest bit, cost O(len(xor_pair)) time each loop
    for ind in range(first1_ind+1, 32):  # first1_ind+1 ~ 32
        # print (xor_pairs)
        keep_pair = []
        for x, y in xor_pairs:
            if x[ind] != y[ind]:
                keep_pair.append((x, y))
        if len(keep_pair) > 0:
            xor_pairs = keep_pair
        else:
            continue
    print ("xor pairs ", len(xor_pairs))
    # This step can be optimized by comparing which pairs have higher different bit value
    # when len(l) is bigger than 10^6 etc, it has performance impact 
    val = max([int(x, 2)^int(y, 2) for x, y in xor_pairs])
    return val
        

### Test case, the naive version has exact the same output with the bit moving version

test1 = [*range(100, 5000)] + [100000]      # Test bit moving best condition
# test1 = [*range(100, 10000)]                # Test the worst/sequence case
# test1 = [4, 5, 6, 7]                          # b 100, 101, 110, 111
# test1 = [*range(8, 16)]                       # b 1000~1111
# test1 = [2, 5, 6, 8]                        # Simple Test


import time
s1 = time.time()
print (find_max_xor(test1))
e1 = time.time()
print ("elasped: {}".format(e1-s1))

# 1000 -> 0.23s     10000 -> 21.2s

# Time: O(N^2)  Mem: O(1)

s1 = time.time()
print (find_max_xor2(test1))
e1 = time.time()
print ("elasped: {}".format(e1-s1))

# 1000 -> 0.13s     10000 -> 8.88s

# XOR/XOR2 Sequence case evaluated:
# O(numbit * K * M) -> K+M=N
# XOR2: Worst: O(N*N/4), Mem: O(N*M/4)

# XOR/XOR2 Best case evaluated:
# XOR2 Best: O(numbit * N) -> O(N), Mem: O(N) # only one highest bit is 1
# test1 = [*range(100, 5000)] + [100000]
# XOR: 5.05s vs. XOR2 0.008s
