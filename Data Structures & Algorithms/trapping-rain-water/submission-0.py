class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) - 1
        max_prefix = 0
        max_suffix = 0
        prefixes = [0] * len(height)
        suffixes = [0] * len(height)
        for i, h in enumerate(height):
            if i == 0:
                continue
            if height[i - 1] > max_prefix:
                max_prefix = height[i - 1]
            if height[n - i + 1] > max_suffix:
                max_suffix = height[n - i + 1]
            prefixes[i] = max_prefix
            suffixes[n - i] = max_suffix
        max_area = 0
        filled_bars = []
        for i, h in enumerate(height):
            area = min(prefixes[i], suffixes[i]) - h
            filled_bars.append(area)
            if area > 0:
                max_area += area
        # print(prefixes)
        # print(suffixes)
        # print(filled_bars)
        return max_area

            



        
