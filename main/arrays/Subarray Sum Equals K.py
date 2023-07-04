Input: nums = [3,4,7,2,-3,1,4,2], k = 7
Output: 4

# Brute force way

res=0
for i in range(len(nums)):
  count=0
  for j in range(i,len(nums)):
    count+=nums[j]
    if count==k:
      res+=1
print(res)


# optimised solution using hash map

hash={0:1}
sum=0
res=0
for i in range(len(nums)):
  sum+=nums[i]
  res+=hash.get(sum-k,0)
  hash[sum]=1+hash.get(sum,0) 
print(res)



# Subarray with given sum
# brute force finding indexes

for i in range(len(arr)):
  sum1=0
  for j in range(i,len(arr)):
    sum1+=arr[j]
    if sum1==s:
      return [i+1,j+1]
return [-1]


# optimised way

if s==0:
  return [-1]
res=0
l=0
sum1=0
for i in range(len(arr)):
  sum1+=arr[i]
  while sum1>s:
    sum1-=arr[l]
    l+=1
  if sum1==s:
    return [l+1,i+1]
return [-1]

