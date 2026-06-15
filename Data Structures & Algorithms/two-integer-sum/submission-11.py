#Making a Hashmap and searching for target - num directly
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:      # O(1) dict lookup
                return [seen[complement], i]
            seen[num] = i                # O(1) dict insert