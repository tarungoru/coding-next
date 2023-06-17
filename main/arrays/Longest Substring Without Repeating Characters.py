Input: s = "abcabcbb"
Output: 3
  
# "optimised solution" using the array
res=[]
c=0
ct=0
for i in range(len(s)):
  while res and (s[i] in res):
    res.pop(0)
    c-=1
  res.append(s[i])
  c+=1
  ct=max(ct,c)
print(ct)
  
# optimised solution using the set

res=set()
c=0
ct=0
for i in range(len(s)):
  while(s[i] in res):
    res.remove(s[c])
    c+=1
  res.add(s[i])
  ct=max(ct,i-c+1)
print(ct)
