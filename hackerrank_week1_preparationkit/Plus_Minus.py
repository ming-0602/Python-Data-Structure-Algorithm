def plusMinus(arr):
    # Write your code here

    total_positive = 0
    total_negative = 0
    total_zero = 0

    for arrs in arr:
        if (arrs > 0):
            total_positive += 1
        if (arrs < 0):
            total_negative += 1
        if (arrs == 0):
            total_zero += 1

    size_of_array = len(arr)

    print(f"{total_positive / size_of_array:6f}")
    # print(Decimal(total_positive) // Decimal(len(arr)))
    print(f"{total_negative / size_of_array:6f}")
    print(f"{total_zero / size_of_array:6f}")

plusMinus([1,2,3,4,5,6])