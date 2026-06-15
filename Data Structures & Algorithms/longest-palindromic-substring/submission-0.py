class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Odd-length palindromes (single center)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1 # After loop: left < 0 or s[left] != s[right], so valid range is (left+1, right-1)
            if right - left - 1 > end - start:
                start = left + 1
                end = right
            
            # Even-length palindromes (double center)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start = left + 1
                end = right
        
        return s[start:end]

        