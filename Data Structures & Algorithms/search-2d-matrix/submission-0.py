class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowToSearch = 0

        lo = 0
        hi = len(matrix)-1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][-1] < target:
                lo = mid + 1
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                low = 0
                high = len(matrix[mid])-1

                while low <= high:
                    middle = (low + high) // 2
                    if matrix[mid][middle] < target:
                        low = middle + 1
                    elif matrix[mid][middle] > target:
                        high = middle - 1
                    else:
                        return True
                return False
        return False