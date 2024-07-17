# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Time complexity O(n)
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ans = []
        toDeleteSet = set(to_delete)

        def dfs(root, isRoot):
            if not root:
                return None
            deleted = root.val in toDeleteSet
            if isRoot and not deleted:
                ans.append(root)
            
            root.left = dfs(root.left, deleted)
            root.right = dfs(root.right, deleted)
            return None if deleted else root
            
        dfs(root, True)
        return ans
