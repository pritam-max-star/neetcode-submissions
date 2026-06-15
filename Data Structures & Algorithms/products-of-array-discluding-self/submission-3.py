class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            new_list = [x for j, x in enumerate(nums) if j != i]
            prod = 1
            for j in range(len(new_list)):
                prod *= new_list[j]
            result.append(prod)
        return result
        