#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.


def get_primes(num):
    l = [2]
    for i in range(2, num):
        flag = True
        for j in l:
            # 如果当前值可整除已筛选出的素数中的任意值，则改变flag，结束循环
            if i % j == 0:
                flag = False
                break
        if flag is True:        # is Prime
            l.append(i)
    return l


# Sliding window to find the number of the sum value

def main(s, num):
    primes = get_primes(num)
    left, right = 0, 1      # [)

    sliding_sum = 2     # sum of the sliding window
    count = 0           # the number of combination

    while right <= len(primes) and primes[right-1] <= s:
        # print (sliding_sum, s)
        if sliding_sum == s:
            # print (left, right)
            # print (primes[left:right+1])
            count += 1
            # 注意减的时候要先从sum里面减掉，
            # 再改变left index，否则就减错位置了
            sliding_sum -= primes[left]
            left += 1
            # OR
            # right += 1
            # sliding_sum += primes[right]
        elif sliding_sum > s:
            sliding_sum -= primes[left]
            left += 1
        else:   # sliding_sum < s
            # 加的时候需要从先加right，改变index
            # 再改变sum的值
            sliding_sum += primes[right]
            right += 1

    return count

print (main(41, 10000))
