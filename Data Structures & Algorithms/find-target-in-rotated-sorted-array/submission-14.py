class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        start = 0
        end = len(nums) - 1
        left = nums[start]
        right = nums[end]
        mid_idx = start
        mid_item = left
        while left > right:
            mid_idx = (start + end) // 2
            mid_item = nums[mid_idx]
            if mid_item == left:
                if left < right:
                    # print(f'left')
                    break
                mid_idx = mid_idx + 1
                mid_item = nums[mid_idx]
                # print('right')
                break
            if mid_item > left:
                start = mid_idx
                left = nums[start]
            else:
                end = mid_idx
                right = nums[end]
        min_idx = mid_idx
        min_item = mid_item
        print(f'min_item: {min_item}')
        if target > nums[-1]:
            start = 0
            end = min_idx - 1
        else:
            start = min_idx
            end = len(nums) - 1
        left = nums[start]
        right = nums[end]
        print(f'start: {start}')
        print(f'end: {end}')
        print(f'left: {left}')
        print(f'right: {right}')
        while start < end:
            mid_idx = (start + end) // 2
            mid_item = nums[mid_idx]
            print(f'mid_item: {mid_item}')
            print(f'target: {target}')
            if target == mid_item:
                return mid_idx
            if target > mid_item:
                start = mid_idx + 1
                left = nums[start]
            else:
                end = mid_idx
                right = nums[end]
            print(f'start: {start}')
            print(f'end: {end}')
            print(f'left: {left}')
            print(f'right: {right}')
        if start == end and target == left:
            return start
        return -1 
