class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        L = self.sortArray(nums[:mid])
        R = self.sortArray(nums[mid:])

        result = []
        i = j = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        result.extend(L[i:])
        result.extend(R[j:])
        return result