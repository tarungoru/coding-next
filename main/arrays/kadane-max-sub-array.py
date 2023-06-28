Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Brute force solution

if len(nums)==1:
  print(nums)
res=-10**9
for i in range(len(nums)):
  for j in range(i,len(nums)):
    sum=0
    for k in range(i,j+1):
      sum+=nums[k]
    res=max(res,sum)
print(res)


# optimised code

res,sum=-10**9,0
for i in range(len(nums)):
  if sum<0:
    sum=0
  sum+=nums[i]
  res=max(res,sum)
print(res)
