# 8624 ms	14.5 MB
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            else:
                if nums[i] + nums[j] == target:
                    return [i, j]
