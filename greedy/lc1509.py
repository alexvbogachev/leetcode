class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# O(n) time complexity 
        if len(nums) <= 4:
            return 0

        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))
        result = float("inf")
        for i in range(4):
            result = min(
                result, max_four[i] - min_four[i]
            )
        return result

# O(nlogn) time complexity solution
#        if len(nums) <= 4:
#            return 0

#        nums.sort()
#        result = float("inf")
#        for l in range(4):
#            r = len(nums) - 4 + l
#            result = min(
#                result,
#                nums[r]-nums[l]
#            )
#        return result
