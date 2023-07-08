Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

# brute force code 

if len(s)<3:
return 0
res=0
for i in range(len(s)):
  flag=True
  stack=[]
  if 3+i>len(s):
    break
  for i in range(i,3+i):
    if s[i] not in stack:
      flag=True
      stack.append(s[i])
    else:
      flag=False
      break
  res+=1 if flag else 0
  print(res)



# optimised code

if len(s)<3:
  return 0
res=0
a=s[0]
b=s[1]
c=s[2]
for i in range(3,len(s)):
  if a!=b and b!=c and c!=a:
    res+=1
    a,b,c=b,c,s[i]
if a!=b and b!=c and c!=a:
  res+=1
return res
