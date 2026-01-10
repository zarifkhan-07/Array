def eq(arr):
    total_sum=sum(arr)
    left_sum=0
    for i in range(len(arr)):
        total_sum=total_sum+arr[i]
        if left_sum==total_sum:
            return i
        left_sum=left_sum+arr[i]
    return -1
arr=[-1,3,5,2]
index=eq(arr)
if index!=-1:
    print("Equilibriam index is:",index)
else:
    print("No equllibriam index found")