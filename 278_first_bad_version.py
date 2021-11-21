# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1
        start = 1
        end = n
        while start<=end:
            print(start,end)
            temp = (start+end)//2
            if isBadVersion(temp):
                end = temp-1
                continue
            elif isBadVersion(temp+1):
                return temp+1
            else:
                start = temp+1
                
    
        
