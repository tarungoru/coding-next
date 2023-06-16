"brute force solution"

Input: prices = [7,1,5,3,6,4]
Output: 5


res=0
for i in range(len(prices)):
  for j in range(i+1,len(prices)):
    res=max(res,prices[j]-prices[i])
print(res)


"optimal solution using sliding window"

res=0
left=prices[0]
for i in range(1,len(prices)):
  res=max(res,prices[i]-left)
  if prices[i]-left<0:
    left=prices[i]
print(res)

"optimal solution using two pointers"

res=0
l,r=0,1
while r<len(prices):
  if prices[l]>prices[r]:
    res=max(res,prices[r]-prices[l])
  else:
    l=r
  r+=1
print(res)



