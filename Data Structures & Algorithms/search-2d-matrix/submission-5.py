class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start != end:
            mid_idx = (start + end) // 2
            mid = matrix[mid_idx]
            if mid[0] < target and mid[-1] < target:
                start = mid_idx + 1
            else:
                end = mid_idx
        row_idx = start
        nums = matrix[row_idx]
        start = 0
        end = len(nums) - 1
        while start != end:
            mid_idx = (start + end) // 2
            mid = nums[mid_idx]
            if mid == target:
                return True
            elif mid < target:
                start = mid_idx + 1
            else:
                end = mid_idx
        if nums[start] == target:
            return True
        return False
            