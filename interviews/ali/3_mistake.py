def find_max_xor(l):
    vals = []
    for x in l:
        for y in l:
            if y != x:
                val = x^y
                vals.append(val)
    
    return max(vals)

def to_binstr(x):
    return '{0:08b}'.format(x)



def find_max_xor2(l):
    val_s = [to_binstr(x) for x in l]
    
    # find the first 1 loc
    for i, c in enumerate(val_s):
        if c == "1":
            first1_loc = i
            break
    
    # build other strings
    other_val_s = []
    for i, x in enumerate(l):
        if i != max_val_id:
          other_val_s.append(to_binstr(x))
    print (max_val_s)
    print (other_val_s)
    # print(other_val_s)
    # print (first1_loc)
    # print (max_val)
    # print ("-----------")
    for i in range(first1_loc, 8):		# 0~7 actually
        # keep all indexes that differences with the max_val
        keep_ind = []
        for j, x in enumerate(other_val_s):
            if x[i] != max_val_s[i]:
                keep_ind.append(j)

        # update other_val_s
        if len(keep_ind) > 0:
            new_other_val_s = []
            for k in keep_ind:
                new_other_val_s.append(other_val_s[k])
            other_val_s = new_other_val_s
        else:
            other_val_s = other_val_s
        print (other_val_s)
    
    # fetch max value
    other_vals = [int(x, 2) for x in other_val_s]
    print (other_vals)
    val = max([(x ^ max_val) for x in other_vals])

    return val

print (find_max_xor([8, 10, 2]))
print (find_max_xor2([8, 10, 2]))

# print(find_max_xor([int("0101", 2), int("1100", 2), int("0101", 2)]))
# print (int("1100", 2) ^ int("1001", 2))