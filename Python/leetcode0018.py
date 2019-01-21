#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0018.py

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
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
    注意：
    答案中不可以包含重复的四元组。

    示例：
    给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
    满足要求的四元组集合为：
    [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
    ]
    """
    @performance
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort() # 将nums按照从小到大排序
        
        L = []
        if len(nums) < 4:
            return L

        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i-1]): # 去重
                continue
            for j in range(i+1, len(nums)):
                if (j > i+1) and (nums[j] == nums[j-1]): # 去重
                    continue
                m = j + 1
                n = len(nums) - 1
                while(m < n):
                    x = nums[i] + nums[j] + nums[m] + nums[n]
                    #print "nums[%d] + nums[%d] + nums[%d] + nums[%d]:%d + %d + %d + %d = %d" % (i, j, m, n, nums[i], nums[j], nums[m], nums[n], x)
                    if x < target:
                        m += 1
                    elif x > target:
                        n -= 1
                    else:
                        #print "nums[%d] + nums[%d] + nums[%d] + nums[%d]:%d + %d + %d + %d = %d" % (i, j, m, n, nums[i], nums[j], nums[m], nums[n], x)
                        if (m > j+1) and (nums[m] == nums[m-1]): # 去重
                            pass
                        else:
                            L.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1
        return L

if __name__ == '__main__':
    solution = Solution()

    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)