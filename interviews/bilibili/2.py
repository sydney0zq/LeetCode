#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""

"""
l=[2]
for i in range(2,10000):
    flag=True
    for j in l:
        if i%j==0:#如果当前值可整除已筛选出的素数中的任意值，则改变flag，结束循环
            flag=False
            break
    if flag:#添加该数至素数列表
        l.append(i)
n=41
left = right=0
sum=2
output=0
while(l[right]<=n):
    if sum==n:
        output+=1
    if sum>=n:
        sum -=l[left]
        left+=1
    else:
        right+=1
        if right>len(l):
            break
        sum += l[right]
print(output)
