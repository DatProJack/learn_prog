nums=[1,2,3,4,5,7,9,78,43,65,12,34]
large=0
for i in range(0,len(nums)):
    if(nums[i]>large):
        large=nums[i]
print(large)
