#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""
https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
"""

# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:

        # Naive version
        #max_num = 10 ** n
        #return [*range(1, max_num)]
        
        # Recursively
        res = []
        temp = ['0'] * n
        def helper(index):
            if index == n:
                res.append(int(''.join(temp)))
                #print (int(''.join(temp)))
                return
            for i in range(10):
                temp[index] = chr(ord("0") + i)
                helper(index+1)
        helper(0)
        return res[1:]






print (Solution().printNumbers(3))




