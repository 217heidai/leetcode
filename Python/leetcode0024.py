#!/usr/bin/python3
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0024.py

import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print ("call %s() in %fs" % (f.__name__, (t2-t1)))
        return r
    return fn

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    
    示例:
    给定 1->2->3->4, 你应该返回 2->1->4->3.
    """
    @performance
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None) or (head.next == None):
            return head

        # 为了方便调换，增加一个临时头节点
        tempHead = ListNode(0)
        tempHead.next = head

        first  = head.next
        second = tempHead

        while(first != None):
            tmp1 = second.next
            tmp2 = first.next
            second.next = first
            second.next.next = tmp1
            second.next.next.next = tmp2
            first = second.next.next

            if first.next != None:
                second = first
                first  = first.next.next
            else:
                break

        return tempHead.next


if __name__ == '__main__':
    def CreatListNode(values):
        if values == None or len(values) < 1:
            return None
        head = ListNode(values[0])
        node = head
        for i in range(1,len(values)):
            node.next = ListNode(values[i])
            node = node.next
        node.next = None
        return head
    
    def PrintListNode(ln):
        disp = ''
        while(ln != None):
            disp += "%d->" % (ln.val)
            ln = ln.next
        print("%s" % (disp[:-2]))

    solution = Solution()
    l1 = CreatListNode((1,2,3,4))
    PrintListNode(l1)
    PrintListNode(solution.swapPairs(l1))

    l2 = CreatListNode((1,2,3,4,5))
    PrintListNode(l2)
    PrintListNode(solution.swapPairs(l2))

    l3 = CreatListNode((1,))
    PrintListNode(l3)
    PrintListNode(solution.swapPairs(l3))

    l4 = CreatListNode(None)
    PrintListNode(l4)
    PrintListNode(solution.swapPairs(l4))

    l5 = CreatListNode((1,2))
    PrintListNode(l5)
    PrintListNode(solution.swapPairs(l5))