class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        
        while l < r:  # strict < so we don't overshoot
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                # min is in the right half
                l = m + 1
            else:
                # nums[m] <= nums[r], min is m or to the left
                r = m  # don't do m-1, m itself could be the min
        
        return nums[l]  # l == r at this point
        