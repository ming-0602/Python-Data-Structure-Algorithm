def mergersort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = mergersort(left)
    right = mergersort(right)

    return recsort(left, right)

def recsort(left , right):

    result = []

    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            # k +=1
        else:
            result.append(right[j])
            j += 1
            # k += 1


    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


arr = [783, 523, 510, 926, 31, 315, 972, 877]

print(mergersort(arr))














# arr = [9, 7, 4, 2, 1, 5, 8, 3, 6]
