#pivot num
nums = [1, 7, 3, 6, 5, 6]
for index in range(len(nums)):
 sum=0
 d=0
 for i in range(0,index):
    sum=sum+nums[i]
 for j in range(index+1,len(nums)):
    d=d+nums[j]
 if sum==d:
    print(nums[index],"it is pivot num")
    break

else:
    print(-1)






