class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:       # this element is a keeper
                nums[k] = nums[i]    # place it at position k
                k += 1               # move k forward
        return k
        