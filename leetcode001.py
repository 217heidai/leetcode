#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode.py

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
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    """
    @performance
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if target == nums[i] + nums[j]:
                    return [i, j]
        return [0, 0]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    targer = 9
    
    solution = Solution()
    print solution.twoSum(nums, targer)
