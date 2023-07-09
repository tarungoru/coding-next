Input: nums = [3,4,5,1,2]
Output: true

# optimised code

count=0
index=0
for i in range(len(nums)-1):
  if nums[i]>nums[i+1]:
    count+=1
    index=i+1
if count==0:
  print(True)
elif count==1:
  arr=nums[index:]+nums[:index]
  for i in range(len(arr)-1):
    if arr[i+1]<arr[i]:
      print(False)
  print(True)
else:
  print(False)
