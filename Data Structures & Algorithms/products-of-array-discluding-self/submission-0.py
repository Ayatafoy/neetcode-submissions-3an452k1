class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(len(nums)):
            prefix = 1
            suffix = 1
            i = 0
            j = 0
            while i < index:
                prefix *= nums[i]
                i += 1
            while j < len(nums):
                if j <= index:
                    j += 1
                    continue
                suffix *= nums[j]
                j += 1
            result.append(prefix * suffix)
        return result