class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        while s<=e:
            mid = (s+e)//2
            #print(s,e,mid)
            if nums[mid]>target:
                if nums[s]<=target:
                    e=mid-1
                elif nums[s]>target and nums[mid]<=nums[s] and mid!=s:
                    e=mid-1
                else:
                    s=mid+1
            elif nums[mid]<target:
                if nums[e]>=target:
                    s=mid+1
                elif nums[e]<target and nums[mid]>=nums[e] and mid!=e:
                    s=mid+1
                else:
                    e=mid-1
            else:
                return mid
        return -1
        
