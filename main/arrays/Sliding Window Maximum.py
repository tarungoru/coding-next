Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

# brute force approach

res=[]
for i in range(len(arr)):
  max_sum=0
  if k>len(arr):
    return res
  for j in range(i,k):
    if arr[j]>max_sum:
      max_sum=arr[j]
      res.append(max_sum)
      k+=1
return res
# quite optimised approach
ans=[]
heap=[]
for i in range(k):
  heapq.heappush(heap,[-arr[i],i])
  ans.append(-heap[0][0])
for i in range(k,len(arr)):
  heapq.heappush(heap,[-arr[i],i])
  while heap[0][1]<=i-k:
    heapq.heappop(heap)
    ans.append(-heap[0][0])
print(ans)

# optimised approach


