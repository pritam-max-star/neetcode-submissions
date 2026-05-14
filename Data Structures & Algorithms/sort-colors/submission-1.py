import heapq
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        heapq.heapify(nums)
        sorted_vals = [heapq.heappop(nums) for _ in range(n)]
        nums[:] = sorted_vals