Input: N = 7, K = 2
arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: 3 4 5 6 7 1 2
Explanation: Rotation of the above 
array by 2 will make the output array .



class Solution:
    def leftRotate(self, nums, k, n):
        k=k%len(nums)
        if k==0:
            return
        
        def helper(l,r):
            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        helper(0,k-1)
        helper(0,n-1)
        helper(0,n-k-1)
x=solution()
x.leftRotate(nums,k,n)
