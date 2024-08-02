class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time and space complexity
        k = nums.count(1)
        ones = 0
        maxOnes = 0
        for i in range((len(nums))*2):
            if i >= k and nums[i % (len(nums)) - k]:
                ones -= 1
            if nums[i % (len(nums))]:
                ones += 1
            maxOnes = max(maxOnes, ones)
        return k - maxOnes
