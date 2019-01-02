#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0012.py

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
    罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

    示例 1:
    输入: 3
    输出: "III"

    示例 2:
    输入: 4
    输出: "IV"

    示例 3:
    输入: 9
    输出: "IX"

    示例 4:
    输入: 58
    输出: "LVIII"
    解释: L = 50, V = 5, III = 3.

    示例 5:
    输入: 1994
    输出: "MCMXCIV"
    解释: M = 1000, CM = 900, XC = 90, IV = 4.
    """
    @performance
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def Roman(x, Symbol1, Symbol2, Symbol3):
            s = ''
            if x == 0:
                pass
            elif x > 0 and x < 4: # 1～3使用Symbol1，I
                for i in range(x):
                    s += Symbol1
            elif x == 4: # 4使用Symbol1 + Symbol2，IV
                s += Symbol1 + Symbol2
            elif x == 5: # 5使用Symbol2，V
                s += Symbol2
            elif x < 9: # 6~9使用Symbol2 + Symbol1，VI
                s = Symbol2
                for i in range(x - 5):
                    s += Symbol1
            else: # 9使用Symbol1 + Symbol3，IX
                s = Symbol1 + Symbol3
            return s

        m = num/1000%10 # 千位
        n = num/100%10 # 百位
        o = num/10%10 # 十位
        p = num%10 # 各位

        s = ''
        s += Roman(m, 'M', '', '')
        s += Roman(n, 'C', 'D', 'M')
        s += Roman(o, 'X', 'L', 'C')
        s += Roman(p, 'I', 'V', 'X')

        return s


if __name__ == '__main__':
    solution = Solution()

    print solution.intToRoman(3)
    print solution.intToRoman(4)
    print solution.intToRoman(9)
    print solution.intToRoman(58)
    print solution.intToRoman(1994)

