class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(start,end):
            if target>nums[end]:
                return end+1
            if target<nums[start]:
                return start
            temp = (start+end)//2
            if nums[temp]==target:
                return temp
            if nums[temp]<target:
                start = temp+1
            else:
                end = temp-1
            return search(start,end)
        return search(0,len(nums)-1)
        
