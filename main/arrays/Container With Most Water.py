# brute force method

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

  
res=0
for i in range(len(height)):
  for j in range(i+1,len(height)):
    area=(j-i)*min(height[i],height[j])
    res=max(res,area)
print(res)

# optimised solution

res=0
l=0
r=len(height)-1
while l<=r:
  area=(r-l)*min(height[l],height[r])
  if height[l]<=height[r]:
    l+=1
  else:
    r-=1
  res=max(res,area)
print(res)
