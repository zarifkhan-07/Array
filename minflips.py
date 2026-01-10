arr=[1,0,1,0,1,0,1,0]
cnt=0
cnt1=0
for i in range(len(arr)):
    if arr[i]==0:
        cnt+=1
    else:
        cnt1+=1
print("Total flips to make all 0:",cnt)
print("Total flips to make all 1:",cnt1)