#!/usr/bin/python3
# -*- encoding=utf-8 -*- s
# 文件名：leetcode0023.py

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
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

    示例:
    输入:
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    输出: 1->1->2->3->4->4->5->6
    """
    @performance
    def mergeKLists(self, lists): # 所有节点插入一个列表直接排序，再重新组成链表
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        L = []
        for item in lists:
            node = item
            while(node != None):
                L.append(node)
                node = node.next
        L.sort(key=lambda node:node.val, reverse=False)

        if len(L) < 1:
            return None

        head = L[0]
        node = head
        for i in range(1,len(L)):
            node.next = L[i]
            node = node.next
        node.next = None

        return head


if __name__ == '__main__':
    def CreatListNode(values):
        if len(values) < 1:
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
    
    lists = []
    l1 = CreatListNode((1,4,5))
    PrintListNode(l1)
    lists.append(l1)
    
    l2 = CreatListNode((1,3,4))
    PrintListNode(l2)
    lists.append(l2)
    
    l3 = CreatListNode((2,6))
    PrintListNode(l3)
    lists.append(l3)

    solution = Solution()
    PrintListNode(solution.mergeKLists(lists))
