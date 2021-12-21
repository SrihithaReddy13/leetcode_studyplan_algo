class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        s=0
        e = n-1
        arr=-1
        while s<=e:
            mid=(s+e)//2
            if matrix[mid][0]<=target:
                if mid!=n-1 and matrix[mid+1][0]<=target:
                    s=mid+1
                else:
                    arr = mid
                    break
            elif matrix[mid][0]>target:
                e=mid-1
            else:
                s=mid+1
        if arr==-1:
            return False
        s=0
        e=len(matrix[0])-1
        while s<=e:
            mid=(s+e)//2
            if matrix[arr][mid]>target:
                e=mid-1
            elif matrix[arr][mid]<target:
                s=mid+1
            else:
                return True
        return False
            
