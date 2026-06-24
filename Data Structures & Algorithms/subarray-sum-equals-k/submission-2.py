class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}  # prefix_sum -> frequency
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            
            # If (prefix_sum - k) exists, those many subarrays end here with sum k
            res += prefix_count.get(prefix_sum - k, 0)
            
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return res