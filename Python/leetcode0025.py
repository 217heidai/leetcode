#!/usr/bin/python3
# -*- encoding=utf-8 -*- s
# filename: leetcode0025.py

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
    给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

    示例 :
    给定这个链表：1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5

    说明 :
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    """
    @performance
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverseListNode(head): #翻转链表
            if(head == None) or (head.next == None): #None或单个节点无需翻转
                return head
            
            first = head.next
            second = head

            while(first != None):
                tmp = first.next
                first.next = second
                second = first
                first = tmp

            newEnd = head
            newHead = second
            return newHead, newEnd # 返回头、尾节点

        if (head == None) or (head.next == None) or (k < 2):
            return head

        i = 1
        preNode = None
        current = head
        tmpHead = head
        while(current != None):
            if i == k:
                nextNode = current.next
                current.next = None
                newHead, newEnd = reverseListNode(tmpHead)
                #上一个节点指向新头节点
                if preNode != None:
                    preNode.next = newHead
                else:
                    head = newHead
                #新尾节点指向下一个节点
                newEnd.next = nextNode
                tmpHead = nextNode
                preNode = newEnd
                i = 1
                current = tmpHead
                continue
            current = current.next
            i += 1

        return head


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
    l1 = CreatListNode((1,2,3,4,5))
    PrintListNode(l1)
    PrintListNode(solution.reverseKGroup(l1,2))

    l2 = CreatListNode((1,2,3,4,5))
    PrintListNode(l2)
    PrintListNode(solution.reverseKGroup(l2,3))
    l3 = CreatListNode((1,))
    PrintListNode(l3)
    PrintListNode(solution.reverseKGroup(l3,2))

    l4 = CreatListNode(None)
    PrintListNode(l4)
    PrintListNode(solution.reverseKGroup(l4,2))

    l5 = CreatListNode((1,2))
    PrintListNode(l5)
    PrintListNode(solution.reverseKGroup(l5,2))