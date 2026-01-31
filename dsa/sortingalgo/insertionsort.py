def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            tem = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tem
            j -= 1

arr = [38, 27, 43, 10]

insertion_sort(arr)

print(arr)