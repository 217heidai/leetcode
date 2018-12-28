#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0004.py

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
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0

    示例 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
    """
    @performance
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def Insert(L, num):
            left = 0
            right = len(L) - 1
            while(left <= right): # 二分查找插入位置
                mid = (left + right)/2
                if left < right:
                    if L[mid] < num:
                        left = mid + 1
                    elif L[mid] > num:
                        right = mid - 1
                    else:
                        break # 找到相同值的项
                else:
                    if L[mid] < num: # 列表项小于插入项则下标+1，否则使用相同小标替代原值
                        mid += 1
                    break
            #print "left:%d, right:%d, mid:%d" % (left, right, mid)
            if mid > len(L) - 1:
                return L + [num,]
            else:
                return L[:mid] + [num,] + L[mid:]
        
        if len(nums1) >= len(nums2):
            temp = nums1
            temp1 = nums2
        else:
            temp = nums2
            temp1 = nums1
        for item in temp1:
            #print "item:%d, temp:%s" % (item, ",".join(map(lambda item:str(item), temp)))
            temp = Insert(temp, item)
            #print "item:%d, temp:%s" % (item, ",".join(map(lambda item:str(item), temp)))
        
        if len(temp) %2 == 0:
            return (temp[len(temp)/2 - 1] + temp[len(temp)/2]) / 2.0
        else:
            return  temp[len(temp)/2] * 1.0
                    



if __name__ == '__main__':
    solution = Solution()

    nums1 = [1, 3]
    nums2 = [0]
    print solution.findMedianSortedArrays(nums1, nums2)

    nums1 = [1, 3]
    nums2 = [2]
    print solution.findMedianSortedArrays(nums1, nums2)

    nums1 = [1, 3]
    nums2 = [4]
    print solution.findMedianSortedArrays(nums1, nums2)
