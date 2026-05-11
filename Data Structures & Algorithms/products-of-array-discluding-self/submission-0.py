class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# 1 way to do: Find the product of all the elements in the array and everytime divide the i element form th emain product to get the product of other things
        result = []
        product = 1
        zero_count = 0
        for x in nums:
            if x != 0:
                product *= x
            else:
                zero_count += 1
        
        for i in range(len(nums)):
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                result.append(product if nums[i] == 0 else 0)
            else:
                result.append(product // nums[i])
        return result

# 2 way: iterate through the whole thing and have aproduct of the whole thing.

        