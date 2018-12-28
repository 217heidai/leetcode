#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0009.py

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
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:
    输入: 121
    输出: true

    示例 2:
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    
    示例 3:
    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
    """
    @performance
    def isPalindrome(self, x): # 转为字符串处理
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if str(x) == str(x)[::-1]:
            return True
        
        return False
    
    def isPalindrome1(self, x): # 不转为字符串处理
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        y = 0
        while(x > 0):
            y = y*10 + x%10
            x = x/10

        if y != tmp:
            return False
        return True

if __name__ == '__main__':
    solution = Solution()

    print solution.isPalindrome(12321)
    print solution.isPalindrome(-1)
    print solution.isPalindrome(123)

