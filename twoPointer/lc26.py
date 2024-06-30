# O(n) time complexity with two pointers.
class Solution(object):
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

# Solution that runs faster in leetcode but is O(n logn)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Remove duplicates and sort in place
        nums[:] = sorted(set(nums))
        return len(nums)
