from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # most_common() returns highest first, so reverse for stack
        stk = [num for num, freq in c.most_common()[::-1]]
        result = []
        while k > 0:
            result.append(stk.pop())
            k -= 1
        return result

