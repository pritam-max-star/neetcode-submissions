class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        n = len(s)
        result = []

        for m in range(n):
            if m > 0 and s[m] == s[m - 1]:
                continue

            l = m + 1
            r = n - 1

            while l < r:
                total = s[m] + s[l] + s[r]

                if total == 0:
                    result.append([s[m], s[l], s[r]])

                    l += 1
                    r -= 1

                    while l < r and s[l] == s[l - 1]:
                        l += 1

                    while l < r and s[r] == s[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return result