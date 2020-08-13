#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""

"""

def is_same_form(str1, str2):
    # check the types are the same or not
    t1 = set(str1)
    t2 = set(str2)
    if len(t1-t2) != 0 or len(str1) != len(str2):
        return False
    
    ks = t1
    kv1 = {k:0 for k in ks}
    kv2 = {k:0 for k in ks}
    for x,y in zip(str1, str2):
        kv1[x] += 1
        kv2[y] += 1

    is_same_form = True
    for k in ks:
        if kv1[k] != kv2[k]:
            is_same_form = False
            break

    return is_same_form



#import random
#
#str1 = ["a", "b", "c", "d", "a", "c"]
#str2 = str1.copy()
#random.shuffle(str1)
#str1 = "".join(str1)
#str2 = "".join(str2)
#print (str1)
#print (str2)
#print (is_same_form(str1, str2))


import sys
if __name__ == "__main__":
    inputs = []
    # 读取第一行的n
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        inputs.append(line)
    print (is_same_form(*inputs))
    #print (inputs)













def is_same_form(str1, str2):
    # check the types are the same or not
    t1 = set(str1)
    t2 = set(str2)
    if len(t1-t2) != 0:
        return False
    
    ks = t1
    kv1 = {k:0 for k in ks}
    kv2 = {k:0 for k in ks}
    for x,y in zip(str1, str2):
        kv1[x] += 1
        kv2[y] += 1

    is_same_form = True
    for k in ks:
        if kv1[k] != kv2[k]:
            is_same_form = False
            break

    return is_same_form

import sys
if __name__ == "__main__":
    inputs = []
    for i in range(2):
        line = sys.stdin.readline().strip()
        inputs.append(line)
    print (is_same_form(*inputs))









