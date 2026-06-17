class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # stores last seen index of each char
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1   # jump left pointer
            char_index[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest