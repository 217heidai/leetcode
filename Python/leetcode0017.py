#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0017.py

import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2-t1))
        return r
    return fn


class Solution(object):
    """
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    2:abc
    3:def
    4:ghi
    5:jkl
    6:mno
    7:pqrs
    8:tuv
    9:wxyz
    示例:
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    """
    @performance
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def multiply(L1, L2): # 列表乘法
            L = []
            for item1 in L1:
                for item2 in L2:
                    L.append(item1+item2)
            return L

        if len(digits) < 1:
            return []

        letters = {'2':['a', 'b', 'c'],\
                   '3':['d', 'e', 'f'],\
                   '4':['g', 'h', 'i'],\
                   '5':['j', 'k', 'l'],\
                   '6':['m', 'n', 'o'],\
                   '7':['p', 'q', 'r', 's'],\
                   '8':['t', 'u', 'v'],\
                   '9':['w', 'x', 'y', 'z']}
        L = letters[digits[0]]
        for i in range(1,len(digits)):
            L = multiply(L, letters[digits[i]])
                
        return L


if __name__ == '__main__':
    solution = Solution()

    print solution.letterCombinations('23')
    print solution.letterCombinations('')