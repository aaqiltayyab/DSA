# 4. Median of Two Sorted Arrays


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = sorted(nums1 + nums2)   # merge and sort
        n = len(l)
        if n % 2 == 1:
            return float(l[n // 2])   # middle element
        else:
            return (l[n // 2 - 1] + l[n // 2]) / 2.0

print(Solution().findMedianSortedArrays([1,3],[2]))     # 2.0
print(Solution().findMedianSortedArrays([1,2],[3,4]))   # 2.5
