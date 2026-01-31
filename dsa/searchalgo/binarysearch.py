#the array must be sorted
#split into half to look for the target
#if target is smaller than arr the high = mid -1
#if target is bigger than arr then low = mid + 1
def binarysearch(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1


    return -1

arr = [2, 3, 4, 10, 40]
x = 10

result = binarysearch(arr, x)

print(result)