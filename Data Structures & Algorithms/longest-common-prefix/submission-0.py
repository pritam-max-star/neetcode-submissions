
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # keep trimming prefix until strs[i] starts with it
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]  # chop off last character
                if not prefix:
                    return ""
        
        return prefix


        