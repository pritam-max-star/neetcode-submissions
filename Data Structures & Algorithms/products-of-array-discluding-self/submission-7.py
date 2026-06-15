class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# # 1 way to do: Find the product of all the elements in the array and everytime divide the i element form th emain product to get the product of other things
#         result = []
#         product = 1
#         zero_count = 0
#         for x in nums:
#             if x != 0:
#                 product *= x
#             else:
#                 zero_count += 1
        
#         for i in range(len(nums)):
#             if zero_count > 1:
#                 result.append(0)
#             elif zero_count == 1:
#                 result.append(product if nums[i] == 0 else 0)
#             else:
#                 result.append(product // nums[i])
#         return result

# 2 way: iterate through the whole thing as prefix and suffix left and right and have aproduct of the whole thing.
        n = len(nums)
        result = [1] * n

        # left pass: result[i] = product of everything to the left
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # right pass: multiply by product of everything to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

        