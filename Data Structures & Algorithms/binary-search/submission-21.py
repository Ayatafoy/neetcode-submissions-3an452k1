class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        start = 0
        end = len(nums) - 1
        while start != end:
            mid_idx = (start + end) // 2
            mid = nums[mid_idx]
            if mid == target:
                return mid_idx
            elif mid < target:
                start = mid_idx + 1
            else:
                end = mid_idx
        if nums[start] == target:
            return start
        return -1