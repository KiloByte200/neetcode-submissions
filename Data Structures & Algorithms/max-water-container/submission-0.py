class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        largest_area = 0
        front, back = 0, n-1

        while front < back:
            height_1 = heights[front]
            height_2 = heights[back]

            largest_area = max(largest_area, min(height_1, height_2) * (back-front))

            if height_1 > height_2:
                back -= 1
            elif height_2 > height_1:
                front += 1
            else:
                front += 1
                back -= 1
        return largest_area


           
        