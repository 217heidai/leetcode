#!/usr/bin/python3
# -*- encoding=utf-8 -*- s
# filename: leetcode0029.py

import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print ("call %s() in %fs" % (f.__name__, (t2-t1)))
        return r
    return fn

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。

    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3

    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2

    说明:
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
    """
    @performance
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0) # 判断运算结果的符号
        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        #把除数不断左移，直到它大于被除数
        while divisor <= dividend:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1


if __name__ == '__main__':
    solution = Solution()

    print(solution.divide(10,3))
    print(solution.divide(7,-3))
    print(solution.divide(2147483647,2))