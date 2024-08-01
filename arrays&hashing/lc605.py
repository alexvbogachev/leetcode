class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #Time complexity O(n), space complexity O(1)
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(flowerbed) - 1):
            # Check if current plot and neighbors are all empty
            if flowerbed[i-1:i+2] == [0, 0, 0]:
                # Plant a flower and update count
                flowerbed[i] = 1
                count += 1
            # If enough flowers have been planted, return True
            if count >= n:
                return True
        # Return False if not enough flowers have been planted
        return False
