# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        def critical(prev, curr, nxt):
            return(
                prev.val > curr.val < nxt.val or 
                prev.val < curr.val > nxt.val
            )

        prev, curr = head, head.next
        nxt = curr.next
        min_dist, max_dist = float("inf"), -1
        prev_crit_idx = 0
        first_crit_idx = 0
        i = 1
        while nxt:
            if critical(prev, curr, nxt):
                if first_crit_idx:
                    max_dist = i - first_crit_idx
                    min_dist = min(
                        min_dist,
                        i - prev_crit_idx
                    )
                else:
                    first_crit_idx = i
                prev_crit_idx = i

            prev, curr, nxt = curr, nxt, nxt.next
            i += 1

        if min_dist == float("inf"):
            min_dist = -1 

        return [min_dist,max_dist]
