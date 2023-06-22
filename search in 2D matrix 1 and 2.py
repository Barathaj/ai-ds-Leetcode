class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False

// Another Approach Using Binary Search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        list1 = []
        for row in matrix:
            if row[-1] >= target:
                list1 = row
                break
        l,r = 0,len(list1)-1
        while l <= r:
            mid = (l+r) // 2
            if list1[mid] == target:
                return True
            elif list1[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        
