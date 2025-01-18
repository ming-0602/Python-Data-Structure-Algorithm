def linear_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Move elements of array[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # Place the key in its correct position
        array[j + 1] = key

    # Print the sorted array
    for num in array:
        print(num, end=" ")

if __name__ == "__main__":
    arr = [9, 8, 2, 3, 1, 7, 6, 5, 10, 4]
    linear_sort(arr)