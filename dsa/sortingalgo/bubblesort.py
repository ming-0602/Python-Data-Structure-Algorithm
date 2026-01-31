def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                tem = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tem


arr = [9, 7, 4, 2, 1, 5, 8, 3, 6]

sorted = bubblesort(arr)
print(arr)
