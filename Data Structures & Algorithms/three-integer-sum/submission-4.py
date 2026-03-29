class Solution:
    def two_sum(self, target, nums, duplicates):
        triplets = []
        left_pointer = 0
        right_pointer = len(nums) - 1
        while left_pointer < right_pointer:
            pair_1 = f'{nums[left_pointer]}{nums[right_pointer]}'
            pair_2 = f'{nums[right_pointer]}{nums[left_pointer]}'
            if nums[left_pointer] + nums[right_pointer] == target and not (pair_1 in duplicates or pair_2 in duplicates):
                duplicates.add(pair_1)
                duplicates.add(pair_2)
                triplets.append([-target, nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
            elif nums[left_pointer] + nums[right_pointer] > target:
                right_pointer -= 1
            elif nums[left_pointer] + nums[right_pointer] < target:
                left_pointer += 1
            else:
                left_pointer += 1
                right_pointer -= 1
        return triplets


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_sorted = sorted(nums)
        duplicates = set([])
        for i, fixed in enumerate(nums_sorted):
            triplets = self.two_sum(-fixed, nums_sorted[i+1:], duplicates)
            if len(triplets) > 0:
                result.extend(triplets)
        return result