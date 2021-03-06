#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0002.py

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
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    """
    @performance
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = None
        cur1 = l1
        cur2 = l2
        None_node = ListNode(0)
        exit_flage1 = False
        exit_flage2 = False
        b = 0 # 进位
        while(True):
            a = (cur1.val + cur2.val + b)%10
            b = (cur1.val + cur2.val + b)/10
            #print "cur1:%d, cur2:%d, a:%d, b:%d" % (cur1.val, cur2.val, a, b)
            if l3 == None:
                l3 = ListNode(a)
                cur3 = l3
            else:
                cur3.next = ListNode(a)
                cur3 = cur3.next
            if cur1.next != None:
                cur1 = cur1.next
            else:
                cur1 = None_node
                exit_flage1 = True
            if cur2.next != None:
                cur2 = cur2.next
            else:
                cur2 = None_node
                exit_flage2 = True

            if exit_flage1 and exit_flage2 and b == 0:
                return l3

if __name__ == '__main__':
    def print_list(lc):
        while( lc != None):
            print lc.val
            lc = lc.next

    l1 = ListNode(3)
    l1.next = ListNode(4)
    l1.next.next = ListNode(2)

    l2 = ListNode(4)
    l2.next = ListNode(6)
    l2.next.next = ListNode(5)

    #print_list(l1)
    #print_list(l2)
    solution = Solution()
    lc = solution.addTwoNumbers(l1, l2)
    print_list(lc)