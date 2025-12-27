def leader(arr):
    max_val = arr[-1]
    print(max_val, end=" ")

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
            print(max_val, end=" ")


arr = [16, 17, 4, 19, 5, 2]
leader(arr)
