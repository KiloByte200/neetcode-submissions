class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        for skip in range(n):
            for i in range(n):
                if skip != i:
                    result[skip] *= nums[i]
        return result
        