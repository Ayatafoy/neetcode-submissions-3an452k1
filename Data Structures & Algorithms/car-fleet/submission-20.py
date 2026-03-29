class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        diff = []
        time = []      
        for p in position:
            diff.append(target - p)
        for i, d in enumerate(diff):
            time.append(d / speed[i])
        mapping = {}
        for i, p in enumerate(position):
            mapping[p] = time[i]
        sorted_positions = sorted(position)
        sorted_positions_time = []
        for p in sorted_positions:
            sorted_positions_time.append(mapping[p])
        stack = []
        for t in sorted_positions_time:
            if len(stack) == 0:
                stack.append(t)
            else:
                last_t = stack[-1]
                while t >= last_t and len(stack) > 0:
                    stack.pop()
                    if len(stack) == 0:
                        break
                    last_t = stack[-1]
                stack.append(t)
        return len(stack)



