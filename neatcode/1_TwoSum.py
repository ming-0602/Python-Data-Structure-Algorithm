def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):

            if i != j and nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result

    return result

nums = [2,5,5,11]
target = 10
print(twoSum(nums, target))