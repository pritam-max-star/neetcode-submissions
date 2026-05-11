from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for x in c:
            if c[x] >= abs(n / 2):
                majority = x
        return majority

        