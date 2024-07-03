# Time complexity O(n), space complexity O(1)
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        summation = sum(nums[:k])
        maxSum = summation

        for i in range(len(nums) - k):
            summation = summation - nums[i] + nums[i+k]

            if (summation > maxSum):
                maxSum = summation
        
        return maxSum / float(k)
