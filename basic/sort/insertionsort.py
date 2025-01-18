def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

if __name__ == "__main__":
    # Time complexity is approximately O(n^2) in the worst case

    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]

    insertion_sort(array)

    print(" ".join(map(str, array)))