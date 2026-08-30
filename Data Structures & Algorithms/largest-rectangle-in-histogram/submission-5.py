class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_rect = 0

        for i, height in enumerate(heights + [0]):
            while st and height < heights[st[-1]]:
                popped_index = st.pop()

                left_bound = st[-1] if st else -1
                width = i - left_bound - 1

                max_rect = max(max_rect, width * heights[popped_index])

            st.append(i)

        return max_rect