class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Time complexity O(n4^n), space complexity O(4^n)
        if not digits:
            return []
        digitToLetters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        def dfs(i, path):
            if i == len(digits):
                result.append(''.join(path))
                return
            for letter in digitToLetters[ord(digits[i]) - ord('0')]:
                path.append(letter)
                dfs(i+1, path)
                path.pop()
        dfs(0,[])
        return result
