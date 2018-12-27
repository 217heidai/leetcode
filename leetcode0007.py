#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0007.py

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
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    示例 1:
    输入: 123
    输出: 321

    示例 2:
    输入: -123
    输出: -321

    示例 3:
    输入: 120
    输出: 21
    注意:

    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
    """
    @performance
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2**31 - 1
        min = 2**31

        if (x < 0 - min) or (x > max):
            return 0

        y = abs(x) #取绝对值，转为正数
        z = 0
        while(y > 0):
            #print "y:%d, z:%d" % (y,z)
            z = z * 10 + y%10
            y = y/10

        if x > 0:
            if z > max:
                return 0
            else:
                return z
        else:
            if z > min:
                return 0
            else:
                return 0 - z

        return z


if __name__ == '__main__':
    solution = Solution()

    print solution.reverse(123)
    print solution.reverse(-123)

