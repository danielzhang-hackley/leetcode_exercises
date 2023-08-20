# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        res_cur = res

        l1_cur = l1
        l2_cur = l2
        while l1_cur != None or l2_cur != None:
            if l1_cur == None:
                l1_cur = ListNode()
            if l2_cur == None:
                l2_cur = ListNode()

            res_cur.val += l1_cur.val + l2_cur.val

            if res_cur.val >= 10 or l1_cur.next != None or l2_cur.next != None:
                res_cur.next = ListNode()
                res_cur.next.val += (res_cur.val - (res_cur.val % 10)) // 10
                res_cur.val = res_cur.val % 10

            res_cur = res_cur.next
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next

        return res


solution = Solution()
