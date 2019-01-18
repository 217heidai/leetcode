#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0016.py

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
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
    """
    @performance
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def difference(x, y):
            if x > y:
                return x - y
            else:
                return y - x
                
        nums.sort() # 将nums按照从小到大排序
        threeSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i - 1]): # 不重复
                continue
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                x = nums[i] + nums[j] + nums[k] # 三数之和x
                if x > target: # x>target,则大数应减小k--
                    k -= 1
                elif x < target: # x<target,则小数应增加j++
                    j += 1
                else:
                    return x
                
                if difference(target,x) < difference(target,threeSum):
                    threeSum = x

        return threeSum


if __name__ == '__main__':
    solution = Solution()

    print solution.threeSumClosest([-1, 2, 1, -4], 1)