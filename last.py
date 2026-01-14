def last_no(arr,target):
    last_index=-1

    for i in range(len(arr)):
        if arr[i]==target:
            last_index=i
    
    print(last_index)
arr=[10,20,30,40,50,60,70,80,90,100]
target=20
last_no(arr,target)