class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Time complexity O(n), space complexity O(1)
        freqs = sorted(collections.Counter(word).values(), reverse=True)
        return sum(freq * (i // 8 + 1) for i, freq in enumerate(freqs))
