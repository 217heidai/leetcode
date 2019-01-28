#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0019.py

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
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

    示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
    
    说明：
    给定的 n 保证是有效的。

    进阶：
    你能尝试使用一趟扫描实现吗？
    """
    @performance
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        second = head

        for i in range(n+1):
            if (first != None):
                first = first.next
            else:
                head = head.next
                return head
        
        while(first != None):
            first = first.next
            second = second.next

        second.next = second.next.next

        return head


if __name__ == '__main__':
    def PrintListNode(ln):
        while(ln != None):
            print "%d->" % (ln.val)
            ln = ln.next
        
    def CreatListNode(num):
        ln = ListNode(1)
        current = ln
        for i in range(2, num+1):
            current.next = ListNode(i)
            current = current.next
        return ln

    solution = Solution()

    ln = CreatListNode(1)
    #PrintListNode(ln)

    PrintListNode(solution.removeNthFromEnd(ln, 1))