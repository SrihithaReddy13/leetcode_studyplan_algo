class Solution:
    def findMin(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        e=n-1
        while s<e:
            mid=(s+e)//2
            print(s,e,mid)
            if mid!=0 and nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>=nums[e]:
                s=mid+1
            else:
                e=mid-1
        print("--------")
        return nums[s]
