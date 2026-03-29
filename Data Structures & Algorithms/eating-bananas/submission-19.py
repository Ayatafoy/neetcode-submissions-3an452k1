class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 0
        end = max(piles)
        # print(f'nums: {list(range(max(piles)))}')
        if len(piles) == h:
            return max(piles)
        counter = 0
        while start != end:
            # print(f'start: {start}')
            # print(f'end: {end}')
            cur_h = 0
            mid = (start + end) // 2
            # print(f'mid: {mid}')
            for pile in piles:
                if mid == 0:
                    continue
                cur_h += math.ceil(pile / mid)
            # print(f'cur_h: {cur_h}\n')
            # print(f'h: {h}\n')

            # print(f'--------------')
            if cur_h > h: # speed is too slow, we should increase speed by mooving counter right
                start = mid + 1
            else:
                end = mid
        result = (start + end) // 2
        if result == 0:
            return 1
        return result
