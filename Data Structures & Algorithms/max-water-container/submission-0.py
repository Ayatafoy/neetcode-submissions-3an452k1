class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_area = 0
        while left_pointer < right_pointer:
            heigth = min(heights[left_pointer], heights[right_pointer])
            width = right_pointer - left_pointer
            area = heigth * width
            if area > max_area:
                max_area = area
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            elif heights[left_pointer] > heights[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1
                right_pointer -= 1
        return max_area
