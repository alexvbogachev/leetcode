# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
      # O(logn) time complexity
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val < val:
                curr = curr.right
            else:
                curr = curr.left

        
