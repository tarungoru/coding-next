Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


# optimised code

k=k%len(nums)
l=0
r=len(nums)-1
while l<=r:
  nums[l],nums[r]=nums[r],nums[l]
  l+=1
  r-=1
l=0
r=k-1
while l<=r:
  nums[l],nums[r]=nums[r],nums[l]
  l+=1
  r-=1
l=k
r=len(nums)-1
while l<=r:
  nums[l],nums[r]=nums[r],nums[l]
  l+=1
  r-=1
print(nums)


# small optimised code

k = k % len(nums)
nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])
print(nums)
