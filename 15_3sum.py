class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans= set()
        for i in range(len(nums)):
            #print('i',nums[i])
            target = 0-nums[i]
            #print('target',target)
            d={}
            for j in range(len(nums)):
                #print('j',nums[j])
                if j==i:
                    continue
                temp = target-nums[j]
                #print(d,target)
                if nums[j] in d:
                    arr = [nums[i],nums[j],d[nums[j]]]
                    arr.sort()
                    arr = tuple(arr)
                    ans.add(arr)
                else:
                    d[temp] = nums[j]
                #print(d)
        return ans
                
                
