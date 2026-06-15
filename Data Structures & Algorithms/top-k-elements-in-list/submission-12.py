from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_c = dict(sorted(c.items(), key=lambda x: x[1]))
        stk = []
        result = []
        for x in sorted_c:
            stk.append(x)
        while k > 0:
            result.append(stk.pop())
            k-=1
        return result

