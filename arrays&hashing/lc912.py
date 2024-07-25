class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(nlogn) time complexity
        if len(nums) == 1:
            return nums
        if not nums:
            return []
        pick = random.choice(nums)
        left, mid, right = [], [], []
        for i in nums:
            if i < pick:
                left.append(i)
            elif i > pick:
                right.append(i)
            else:
                mid.append(i)
        return self.sortArray(left) + mid + self.sortArray(right)
