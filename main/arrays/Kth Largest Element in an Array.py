Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

# optimised way

min_value=min(nums)
max_value=max(nums)
count=[0]*(max_value-min_value+1)
for i in nums:
  count[i-min_value]+=1
remain = k
for num in range(len(count) -1, -1, -1):
  remain -= count[num]
  if remain <= 0:
    print(num + min_value)
    break
print(-1)

# using heap

heap = []
for num in nums:
  heapq.heappush(heap,num)
res=[]
while heap:
  res.append(heapq.heappop(heap))
for i in range(k-1):
  res.pop(-1)
print(res[-1])
