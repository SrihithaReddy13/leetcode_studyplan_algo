class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        
        e=n-1
        s=0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return n-1
        while s<=e:
            mid=(s+e)//2
            print(s,e)
            if nums[mid+1]<nums[mid] and nums[mid-1]<nums[mid]:
                return mid
            elif (mid!=n-1 and nums[mid]<nums[mid+1]):
                s=mid+1
            elif (mid!=0 and nums[mid]<nums[mid-1]):
                e=mid-1
                
        return -1
        
