import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapq.heapify(nums)
        sorted_arr = [heapq.heappop(nums) for _ in range(n)]
        nums[:] = sorted_arr
        return nums

        