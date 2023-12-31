arr=[1,0,9,2,5,6,7,10,10]
# Bubble sort
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

# Insertion sort

for i in range(1,len(arr)):
    temp=arr[i]
    j=i-1
    while j>=0 and temp<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
print(arr)

# Selection Sort

for i in range(len(arr)):
    temp=i
    for j in range(i+1,len(arr)):
        if arr[temp]>arr[j]:
            temp=j
    arr[i],arr[temp]=arr[temp],arr[i]
print(arr)

# optimised method o(n) time O(n) space

from collections import Counter
s=Counter(arr)
i=min(arr)
j=max(arr)
res=[]
for i in range(i,j+1):
    if i in s:
        res.extend([i]*s[i])
print(res)

# merge sort

def mergesort(arr):
    if len(arr)==1:
        return
    mid=len(arr)//2
    l=arr[:mid]
    r=arr[mid:]
    mergesort(l)
    mergesort(r)
    i,j,k=0,0,0
    while i<len(l) and j<len(r):
        if l[i]>r[j]:
            arr[k]=r[j]
            j+=1
        else:
            arr[k]=l[i]
            i+=1
        k+=1
    while i<len(l):
        arr[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        arr[k]=r[j]
        j+=1
        k+=1
    return arr
print(mergesort(arr))

# quick sort algorithm


def quickSortUsingDutchNationalFlag(arr):
    def partion(arr,low,high):
        piv=arr[high]
        swap=low-1
        for i in range(low,high):
            if arr[i]<=piv:
                swap+=1
                arr[i],arr[swap]=arr[swap],arr[i]
        arr[high],arr[swap+1]=arr[swap+1],arr[high]
        return swap+1



    def quicksort(arr,low,high):
        if low<high:
            index=partion(arr,low,high)
            quicksort(arr,low,index-1)
            quicksort(arr,index+1,high)
    quicksort(arr,0,len(arr)-1)
    return arr
arr=[1,9,4,2,0]
print(quickSortUsingDutchNationalFlag(arr))
