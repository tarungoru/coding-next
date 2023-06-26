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
