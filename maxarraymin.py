def minimum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = min(temp, arr[i])
    return temp

def maximum(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = max(temp, arr[i])
    return temp

arr = [9, 8, 2, 7, 61, 5]
size = len(arr)

print(minimum(arr, size))
print(maximum(arr, size))
