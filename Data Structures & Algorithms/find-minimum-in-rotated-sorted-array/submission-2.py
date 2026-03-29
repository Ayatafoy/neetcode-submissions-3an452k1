class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        counter = 0
        left = nums[start]
        right = nums[end]
        while left > right:
            mid_idx = (start + end) // 2
            mid_item = nums[mid_idx]
            if mid_item == left:
                if left < right:
                    return left
                else:
                    return right
            if mid_item > left:
                start = mid_idx
                left = nums[start]
            else:
                end = mid_idx
                right = nums[end]
        return left