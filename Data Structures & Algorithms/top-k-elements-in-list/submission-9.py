from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = []
        for num, cnt in c.items():
            l.append([cnt, num])
        l.sort()

        res = []
        while len(res) < k:
            res.append(l.pop()[1])
        return res



