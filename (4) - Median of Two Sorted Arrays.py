# 92 ms
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        if length % 2 == 1:
            return merged[length//2]
        else:
            return (merged[length//2 - 1] + merged[length//2]) / 2

print(Solution.findMedianSortedArrays(Solution, [1,3], [2]))
print(Solution.findMedianSortedArrays(Solution, [1,2], [3,4]))
print(Solution.findMedianSortedArrays(Solution, [0,0], [0,0]))
print(Solution.findMedianSortedArrays(Solution, [], [1]))
print(Solution.findMedianSortedArrays(Solution, [2], []))
