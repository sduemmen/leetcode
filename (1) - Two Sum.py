# 3648 ms	14.5 MB
def twoSum(self, nums: list[int], target: int) -> list[int]:
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
