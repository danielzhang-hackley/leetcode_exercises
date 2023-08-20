# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2) -> ListNode:
        cur = res = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        remain = list1 if list1 else list2
        while remain:
            cur.next = remain

            remain = remain.next
            cur = cur.next

        return res.next

solution = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
x = solution.mergeTwoLists(l1, l2)
while x != None:
    print(x.val)
    x = x.next
