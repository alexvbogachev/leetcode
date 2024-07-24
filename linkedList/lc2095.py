# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Time complexity O(n), space complexity O(1)
        d = ListNode(0, head)
        s = d
        f = d
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        s.next = s.next.next
        return d.next
