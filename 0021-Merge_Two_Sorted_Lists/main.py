# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2) -> ListNode:
        res = ListNode()
        res_cur = res

        list1_cur = list1
        list2_cur = list2

        while list1_cur != None and list2_cur != None:
            if list1_cur.val < list2_cur.val:
                res_cur.val = list1_cur.val
                list1_cur = list1_cur.next
            else:
                res_cur.val = list2_cur.val
                list2_cur = list2_cur.next

            res_cur.next = ListNode()
            res_cur = res_cur.next

        remain_cur = None
        if list1_cur is None:
            remain_cur = list2_cur
        elif list2_cur is None:
            remain_cur = list1_cur

        if remain_cur is None:
            return res

        while remain_cur.next is not None:
            res_cur.val = remain_cur
            res_cur.next = ListNode()
            res_cur = res_cur.next
            remain_cur = remain_cur.next

        res_cur.val = remain_cur.val

        return res


solution = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
x = solution.mergeTwoLists(l1, l2)
while x != None:
    print(x.val)
    x = x.next
