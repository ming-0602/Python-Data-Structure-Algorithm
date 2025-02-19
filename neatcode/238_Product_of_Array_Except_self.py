def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums)) :
        tem_array = nums.copy()
        tem_array.pop(i)
        tem_value = 0
        index = 0
        for j in range(len(tem_array)):
            if index == 0:
                tem_value = tem_array[j]
                index += 1
            else:
                tem_value = tem_value * tem_array[j]
                index += 1

        result.append(tem_value)

    print(result)



nums = [1,2,3,4]
productExceptSelf(nums)