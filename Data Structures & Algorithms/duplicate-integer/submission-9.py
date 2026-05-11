from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # c = Counter(nums)  #Time: O(n) Space: O(n)
        # for x in c:
        #     if c[x] != 1:
        #         return True
        # return False

        #define a stack
        s = set()
        #iterate through nums
        for x in nums:
            if x not in s:
                s.add(x)
            else:
                return True
        return False


                
        #if nums[i] is there in stack, then return true else iterate further and add nums[i] to stack.