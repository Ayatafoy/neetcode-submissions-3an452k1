class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums) - 1
        result = [1] * len(nums)
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        for index in range(n):
            if index != 0:
                prefix *= nums[index - 1]
                suffix *= nums[n - index + 1]
                prefixes[index] = prefix
                suffixes[n - index] = suffix
            else:
                prefixes[index] = math.prod(nums[1:])
                suffixes[n - index] = math.prod(nums[:-1])
            
        for index in range(len(nums)):
            result[index] = prefixes[index] * suffixes[index]   
        return result