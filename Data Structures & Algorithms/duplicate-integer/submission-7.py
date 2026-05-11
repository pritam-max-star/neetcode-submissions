from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # c = Counter(nums)  #Time: O(n) Space: O(n)
        # for x in c:
        #     if c[x] != 1:
        #         return True
        # return False

        #define a stack
        s = []
        #iterate through nums
        for i in range(0, len(nums)):
            if nums[i] not in s:
                s.append(nums[i])
            else:
                return True
        return False


                
        #if nums[i] is there in stack, then return true else iterate further and add nums[i] to stack.