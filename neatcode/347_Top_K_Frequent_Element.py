from collections import defaultdict

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    maparr = dict()
    result = []
    for num in nums:
        maparr[num] = maparr.get(num, 0) + 1

    for i in range(k):
        max_key = max(maparr, key=maparr.get)
        result.append(max_key)
        del maparr[max_key]

    return result



    # while index<k:
    #     maparr.pop(result[index])
    #     index+=1








print(topKFrequent([4,1,-1,2,-1,2,3], 2))