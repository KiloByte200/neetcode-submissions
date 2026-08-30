class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_rect = 0

        for i in range(len(heights)):
            height = heights[i]

            while st and height < heights[st[-1]]:
                popped_index = st.pop()

                left_bound = st[-1] if st else -1
                right_bound = i

                width = right_bound - left_bound - 1
                area = width * heights[popped_index]

                max_rect = max(max_rect, area)

            st.append(i)

        while st:
            popped_index = st.pop()

            left_bound = st[-1] if st else -1
            right_bound = len(heights)

            width = right_bound - left_bound - 1
            area = width * heights[popped_index]

            max_rect = max(max_rect, area)

        return max_rect