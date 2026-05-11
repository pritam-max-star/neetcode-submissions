from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # c = Counter(nums)
        # for x in c:
        #     if c[x] != 1:
        #         return True
        # return False
        # count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False