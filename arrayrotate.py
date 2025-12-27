def rotate(a, k, n):
    k = k % n

    # reverse entire array
    l, r = 0, n - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

    # reverse first k elements
    l, r = 0, k - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

    # reverse remaining elements
    l, r = k, n - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return a
arr=[1,2,3,4,5]
k=2
n=len(arr)
print(rotate(arr,k,n))