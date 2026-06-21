class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        m = len(nums1)
        n = len(nums2)
        sort_nums = sorted(nums)
        print(sort_nums)
        if len(sort_nums) % 2 == 0:
            median = (sort_nums[(m + n)//2 - 1] + sort_nums[(m + n) //2]) / 2
        else:
            median = sort_nums[(m + n) // 2]
        return median

