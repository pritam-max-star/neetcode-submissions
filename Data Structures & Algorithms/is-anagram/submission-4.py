from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s) #Time: O(n) Space: O(n)
        ct = Counter(t)
        return cs == ct

        # sort_s = sorted(s) #Time: O(n logn) Space: O(n)
        # sort_t = sorted(t)
        # return sort_s == sort_t


        