# 3648 ms
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

print(Solution.twoSum(Solution, [2,7,11,15], 9))
print(Solution.twoSum(Solution, [3,2,4], 6))
print(Solution.twoSum(Solution, [3,3], 6))
