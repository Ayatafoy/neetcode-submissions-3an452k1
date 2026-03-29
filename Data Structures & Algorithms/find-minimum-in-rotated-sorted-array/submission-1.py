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
            # print(f'start: {start}')
            # print(f'end: {end}')
            # print(f'left: {left}')
            # print(f'right: {right}')
            mid_idx = (start + end) // 2
            mid_item = nums[mid_idx]
            # print(f'mid_idx: {mid_idx}')
            # print(f'mid_item: {mid_item}\n')
            # print(f'-----')
            if mid_item == left or mid_item == right:
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
            # if counter < 25:
            #     counter += 1
            # else:
            #     break
        return left