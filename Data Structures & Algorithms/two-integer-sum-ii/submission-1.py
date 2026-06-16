class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in numbers:
            if (target - x) in numbers:
                return [numbers.index(x) + 1, numbers.index(target - x) + 1]
        