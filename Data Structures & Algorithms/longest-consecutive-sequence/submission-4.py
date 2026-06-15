class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        max_count = 0

        for x in s:
            if x - 1 not in s:      # only start from sequence beginning
                c = 1
                while x + c in s:   # keep extending the streak
                    c += 1
                max_count = max(max_count, c)
        
        return max_count

        