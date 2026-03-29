class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        groups = []
        for i, h in enumerate(heights):
            groups.append([])
            left_counter = i - 1
            right_counter = i + 1
            groups[i].append(h)
            while left_counter >= 0 and heights[left_counter] >= h:
                groups[i].append(h)
                left_counter -= 1
            while right_counter < len(heights) and heights[right_counter] >= h:
                groups[i].append(h)
                right_counter += 1
        max_area = 0
        for group in groups:
            rectangle_area = sum(group)
            if rectangle_area > max_area:
                max_area = rectangle_area
        return max_area