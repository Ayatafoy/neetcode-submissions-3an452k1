class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 0
        end = max(piles)
        while start != end:
            cur_h = 0
            mid = (start + end) // 2
            for pile in piles:
                if mid == 0:
                    continue
                cur_h += math.ceil(pile / mid)
            if cur_h > h: # speed is too slow, we should increase speed by mooving counter right
                start = mid + 1
            else:
                end = mid
        result = (start + end) // 2
        if result == 0:
            return 1
        return result
