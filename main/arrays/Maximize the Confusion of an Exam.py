"""Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's."""


# brute force code

res=0
cnt1=0
l=0
for r in range(len(ans)):
  if ans[r]=='F':
    cnt1+=1
  while cnt1>k:
      if ans[l]=='F':
        cnt1-=1
      l+=1
  res=max(res,r-l+1)
l=0
cnt2=0
for r in range(len(ans)):
  if ans[r]=='T':
    cnt2+=1
  while cnt2>k:
    if ans[l]=='T':
      cnt2-=1
    l+=1
  res=max(res,r-l+1)
print(res)


# optimised code

maxf=0
ans=0
count={'T':0,'F':0}
n=len(answerKey)
for i in range(n):
    count[answerKey[i]]+=1
    maxf=max(maxf,count[answerKey[i]])
    if ans-maxf<k:
        ans+=1

    else:
        count[answerKey[i-ans]]-=1
print(ans)
