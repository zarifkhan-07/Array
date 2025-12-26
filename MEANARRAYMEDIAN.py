def arraymean(arr):
    total_sum = 0
    for i in range(len(arr)):
        total_sum += arr[i]
    return total_sum / len(arr)

def arraymedian(arr):
    arr = sorted(arr)
    n = len(arr)
    if n % 2 != 0:
        return float(arr[n // 2])
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2.0

arr = [1, 4, 5, 2, 5, 8, 5, 2, 6, 8]

print("mean =", arraymean(arr))
print("median =", arraymedian(arr))
