class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            
            # left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:  # target is in left half
                    r = m - 1
                else:
                    l = m + 1                     # target is in right half
            
            # right half is sorted
            else:
                if nums[m] < target <= nums[r]:  # target is in right half
                    l = m + 1
                else:
                    r = m - 1                     # target is in left half
        
        return -1
            
        