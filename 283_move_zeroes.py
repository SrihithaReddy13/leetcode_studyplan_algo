class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in nums:
            if i==0 :
                break
            zero+=1
        nonzero = 0
        for i in nums:
            if i!=0 and zero<nonzero:
                break
            nonzero+=1
        while zero<len(nums) and nonzero<len(nums):
            nums[zero],nums[nonzero]=nums[nonzero],nums[zero]
            while zero<len(nums) and  nums[zero]!=0:
                zero+=1
            while nonzero<len(nums) and nums[nonzero]==0:
                nonzero+=1
            
        
