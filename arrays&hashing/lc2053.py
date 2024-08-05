class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Time and space complexity O(n)
        count = collections.Counter(arr)
        for a in arr:
            if count[a] == 1:
                k -= 1
                if k == 0:
                    return a
        return ""
