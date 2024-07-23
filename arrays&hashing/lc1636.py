# O(nlogn) time complexity
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = Counter(nums)
        return sorted(nums, key=lambda x: (cnt[x], -x))
