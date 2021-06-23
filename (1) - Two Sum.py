def twoSum(nums, target):

    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 2:
        return [0,1]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            else:
                if nums[i] + nums[j] == target:
                    return [i, j]


print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
print(twoSum(nums = [3,3], target = 6))
print(twoSum(nums = [-1,-2,-3,-4,-5], target = -8))