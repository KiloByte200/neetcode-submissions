class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        curr_min = 1
        curr_max = 1
        result = float("-inf")

        for num in nums:
            temp = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, curr_min * num, curr_max * num)
            curr_max = temp

            result = max(result, curr_max)

        return result

        