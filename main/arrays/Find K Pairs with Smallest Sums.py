Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]

# brute force solution

import heapq

nums1 = [1,2,4,5,6]
nums2 = [3,5,7,9]
k = 3


heap=[]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        heapq.heappush(heap,(nums1[i]+nums2[j],nums1[i],nums2[j]))
res=[]
while k:
    i,j,c=heapq.heappop(heap)
    res.append([j,c])
    k-=1
print(res)



res=[]
heap=[(nums1[0]+nums2[0],nums1[0],nums2[0],0,0)]
visited=set((0,0))
while heap and len(res)<k:
  g,l,m,i,j=heapq.heappop(heap)
  res.append([l,m])
  if i<len(nums1)-1 and (i+1,j) not in  visited:
    heapq.heappush(heap,[nums1[i+1]+nums2[j],nums1[i+1],nums2[j],i+1,j])
    visited.add((i+1,j))
  if j<len(nums2)-1 and (i,j+1) not in visited:
    heapq.heappush(heap,[nums1[i]+nums2[j+1],nums1[i],nums2[j+1],i,j+1])
    visited.add((i,j+1))
print(res)
