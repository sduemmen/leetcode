class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right, ans = 0, len(height) - 1, 0

        while left < right:
            minHeight = height[left] if height[left] < height[right] else height[right]

            area = minHeight * (right -left)
            
            if area > ans:
                ans = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans

print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))