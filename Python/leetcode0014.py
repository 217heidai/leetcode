#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0014.py

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
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    
    说明:
    所有输入只包含小写字母 a-z 。
    """
    @performance
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1: # strs为空，直接返回
            return ''
        elif len(strs) == 1: # strs只有一个值，直接返回该值
            return strs[0]
        if len(strs[0]) < 1: # strs[0]为空，直接返回
            return ''
        
        for i in range(1, len(strs[0]) + 1):
            tmp = strs[0][:i]
            #print "tmp:%s" % (tmp)
            for item in strs:
                if i <= len(item):
                    if item[:i] == tmp:
                        continue
                    else:
                        return tmp[:-1]
                else:
                    return tmp[:-1]
        return tmp


if __name__ == '__main__':
    solution = Solution()

    print solution.longestCommonPrefix(["flower","flow","flight"])
    print solution.longestCommonPrefix(["dog","racecar","car"])
    print solution.longestCommonPrefix([])
    print solution.longestCommonPrefix([''])
    print solution.longestCommonPrefix(["a"])
    print solution.longestCommonPrefix(["a","b"])

