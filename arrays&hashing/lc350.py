# Time ad space complexity O(m+n), where m = len(nums1) and n = len(nums2)
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a,b = map(collections.Counter, (nums1,nums2))
        return list((a&b).elements())
