# O(n) time complexity
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr2=[]
        for i in set(arr):
            if arr.count(i) not in arr2:
                arr2.append(arr.count(i))
            else:
                return False
        return True
