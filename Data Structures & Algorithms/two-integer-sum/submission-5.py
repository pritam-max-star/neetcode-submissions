class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     for j in range(i,n):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        l = []
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                l.append(nums.index(target - nums[i]))
                l.append(i)
                l.sort()
            
        if len(l) > 2:
            return [l[0], l[-1]]
        return l