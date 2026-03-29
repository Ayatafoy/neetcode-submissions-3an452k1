class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] != target:
            return -1
        start = 0
        end = len(nums) - 1
        counter = 0
        while start != end:
            print(f'start: {start}')
            print(f'end: {end}')
            mid_idx = (start + end) // 2
            print(f'mid_idx: {mid_idx}')
            mid = nums[mid_idx]
            print(f'mid: {mid}')
            if mid == target:
                print('mid == target')
                return mid_idx
            elif mid < target:
                print('mid < target')
                start = mid_idx + 1
            else:
                print('mid > target')
                end = mid_idx
            counter += 1
            # if counter == 5:
            #     break
        if nums[start] == target:
            return start
        print(f'start: {start}')
        print(f'end: {end}')
        return -1