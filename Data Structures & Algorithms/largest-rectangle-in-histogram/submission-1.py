class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)        # sentinel
        stack = []               # indices, increasing heights
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area