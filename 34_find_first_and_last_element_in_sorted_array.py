class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        s=0
        e=len(nums)-1
        while s<=e:
            mid = (s+e)//2
            if nums[mid]<target:
                s=mid+1
            elif nums[mid]==target and (mid==0 or nums[mid-1]!=target):
                start = mid
                break
            else:
                e = mid-1
        s=0
        e=len(nums)-1
        while s<=e:
            mid = (s+e)//2
            if nums[mid]>target:
                e=mid-1
            elif nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]!=target):
                end = mid
                break
            else:
                s = mid+1
        return [start,end]
                
                
