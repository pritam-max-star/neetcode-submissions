from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)  #Time: O(n) Space: O(n)
        for x in c:
            if c[x] != 1:
                return True
        return False
        # for i in range(len(nums)): #Time: O(n*2) Space: O(1)
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False