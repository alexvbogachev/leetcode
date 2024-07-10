# O(n) time complexity
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count = 0
        for log in logs:
            if "./" not in log:
                count+=1
            elif "../" in log:
                count=max(0,count-1)
        return count
