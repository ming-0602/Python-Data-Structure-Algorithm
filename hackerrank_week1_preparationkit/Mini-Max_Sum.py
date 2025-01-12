def miniMaxSum(arr):
    # Write your code here

    total_sum = sum(arr)
    tem_arr = []

    for num in arr:
        remove_num_sum = total_sum - num
        tem_arr.append(remove_num_sum)

    min_value = min(tem_arr)
    max_value = max(tem_arr)

    print(f"{min_value} {max_value}")
