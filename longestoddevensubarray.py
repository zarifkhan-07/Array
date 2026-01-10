def longest_alternating(arr):
    if len(arr) == 0:
        return 0

    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2) != (arr[i-1] % 2):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len

arr=[6,4,9,4,7,2,3,4,2,52]
print(longest_alternating(arr))