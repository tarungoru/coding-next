Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

# Brute force code

for i in range(len(nums)):
  for j in range(len(nums)):
    if nums[i]<nums[j]:
      nums[i],nums[j]=nums[j],nums[i]
print(nums)



# optimised code

left=0
right=len(nums)-1
cur=0
while cur<=right:
  if nums[cur]==0:
    nums[cur],nums[left]=nums[left],nums[cur]
    cur+=1
    left+=1
  elif nums[cur]==2:
    nums[cur],nums[right]=nums[right],nums[cur]
    right-=1
  else:
    cur+=1
print(nums)
