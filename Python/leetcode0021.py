#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0021.py

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
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    """
    @performance
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = None
        current1 = l1
        current2 = l2
        head = None
        while True:
            if current1 == None and current2 == None : # current1、current2都为None，则退出
                break
            elif current1 != None and current2 != None : # current1、current2都不为None，则对比大小
                if current1.val < current2.val:
                    tmp = current1
                    current1 = current1.next
                else:
                    tmp = current2
                    current2 = current2.next
                if current == None:
                    current = tmp
                    head = current
                else:
                    current.next = tmp
                    current = current.next
            elif current1 == None: # current1为None，current2不为None，则添加current2
                if current == None:
                    current = current2
                    head = current
                    current2 = current2.next
                else:
                    current.next = current2
                    current = current.next
                    current2 = current2.next
            else: # current2为None，current1不为None，则添加current1
                if current == None:
                    current = current1
                    head = current
                    current1 = current1.next
                else:
                    current.next = current1
                    current = current.next
                    current1 = current1.next
    
        return head


if __name__ == '__main__':
    def PrintListNode(ln):
        while(ln != None):
            print "%d->" % (ln.val)
            ln = ln.next
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    solution = Solution()
    PrintListNode(l1)
    PrintListNode(l2)
    PrintListNode(solution.mergeTwoLists(l1,l2))