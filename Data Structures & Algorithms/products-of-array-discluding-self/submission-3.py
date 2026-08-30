class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        for leftProd in range(1, n):
            result[leftProd] = nums[leftProd - 1] * result[leftProd - 1]
        
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
        