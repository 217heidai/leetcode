#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0020.py

import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2-t1))
        return r
    return fn

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

    示例 1:
    输入: "()"
    输出: true

    示例 2:
    输入: "()[]{}"
    输出: true
    
    示例 3:
    输入: "(]"
    输出: false

    示例 4:
    输入: "([)]"
    输出: false
    
    示例 5:
    输入: "{[]}"
    输出: true
    """
    @performance
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """  
        L = []
        Valid = {'(':')', '[':']', '{':'}'}
        left =  ['(', '[', '{']
        right = [')', ']', '}']

        for char in s:
            if char in left:
                L.append(char)
            elif char in right:
                if (len(L) > 0):
                    if Valid[L[len(L) - 1]] == char:
                        L.pop()
                    else:
                        return False
                else:
                    return False
            else:
                continue

        if (len(L) > 0):
            return False

        return True


if __name__ == '__main__':
    solution = Solution()

    print solution.isValid("()")
    print solution.isValid("()[]{}")
    print solution.isValid("(]")
    print solution.isValid("([)]")
    print solution.isValid("{[]}")