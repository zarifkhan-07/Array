def subarray_sum(arr, target):
    n = len(arr) #4

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum = current_sum + arr[j]

        if current_sum == target:
            print("Subarray found from index", i, "to", j)
            return

    print("No subarray found")

arr = [1, 2, 3, 4]
target = 5
subarray_sum(arr, target)
