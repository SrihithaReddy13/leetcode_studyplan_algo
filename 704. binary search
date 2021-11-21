class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start,end):
            if 0<=start<len(nums) and 0<=end<len(nums):
                if start>end:
                    return -1
                mid = (start+end)//2
                #print(mid)
                if nums[mid] == target:
                    return mid
                elif nums[mid]>target:
                    end = mid-1
                elif nums[mid]<target:
                    start = mid+1
                return binary_search(start,end)
            else:
                return -1
        return binary_search(0,len(nums)-1)
            
        
