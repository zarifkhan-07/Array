def second_largest(arr,size):
    first=second=0
    for i in range(size):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif (arr[i] > second and arr[i] != first):
            second=arr[i]
    if second==0:
        print("There is no second largest number.")
    else:
        print(second)

arr=[7,1,2,3,8,9,6,1,0]
size=len(arr)
second_largest(arr,size)
