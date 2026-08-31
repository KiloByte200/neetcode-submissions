class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(start: int, end: int) -> int:
            prev2 = 0
            prev1 = 0

            for i in range(start, end):
                curr = max(
                    prev1,
                    nums[i] + prev2
                )

                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            rob_line(0, len(nums) - 1),  # exclude last
            rob_line(1, len(nums))       # exclude first
        )