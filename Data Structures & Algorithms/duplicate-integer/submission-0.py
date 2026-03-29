class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_list = len(nums)
        len_set = len(set(nums))
        return len_list != len_set