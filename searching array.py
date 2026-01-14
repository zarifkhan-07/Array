def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr=[1,2,3,4,5,6,7]
x=4

result=search(arr,x)

if result == -1:
    print("The element is not present in the array.")
else:
    print("The element is present at index",result)