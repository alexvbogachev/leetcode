# O(N) time complexity, O(n) memory complexity
class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {} #val:index

        for i, n in enumerate(nums): #iterate through list
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
