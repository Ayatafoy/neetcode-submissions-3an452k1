class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        diffs = [target - x for x in nums]
        has_map = {}
        for i, x in enumerate(nums):
            has_map[x] = i
        for i, diff in enumerate(diffs):
            if diff in has_map and has_map[diff] != i:
                return [i, has_map[diff]]