#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 bytedance <bytedance@FVFCJ0X2L416>
#
# Distributed under terms of the MIT license.

"""
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        new_s = s[n:] + s[:n]
        return new_s


print (Solution().reverseLeftWords("lrloseumgh", 6))


