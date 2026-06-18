class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) % 2
        for m in range(len(nums)):
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
            if nums[m] == target:
                return m
        return -1
                

        