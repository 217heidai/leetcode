#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0022.py

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
    给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

    例如，给出 n = 3，生成结果为：
    [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    ]
    """
    @performance
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def insertParenthesis(l):
            L = []
            for item in l:
                for i in range(1, len(item)):
                    L.append(item[:i] + '()' + item[i:])
                L.append(item + '()')
            return L

        L = ['()']
        for i in range(1, n):
            L = insertParenthesis(L)
            L = list(set(L))

        return L


if __name__ == '__main__':
    solution = Solution()

    print solution.generateParenthesis(4)