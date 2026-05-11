from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        c = Counter(nums)
        sorted_elements = sorted(c.keys(), key=lambda x: c[x], reverse=True)
        l = sorted_elements[:k]
        return l