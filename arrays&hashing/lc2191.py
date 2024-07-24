class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time complexity O(nlogn), space complexity O(n)
        def getMapped(num):
            mapped = []
            for c in str(num):
                mapped.append(str(mapping[ord(c) - ord('0')]))
            return int(''.join(mapped))
        A = [(getMapped(num), i, num) for i, num in enumerate(nums)]
        return [num for _, i, num in sorted(A)]
