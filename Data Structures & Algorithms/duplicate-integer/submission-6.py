from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)  #Time: O(n) Space: O(n)
        for x in c:
            if c[x] != 1:
                return True
        return False