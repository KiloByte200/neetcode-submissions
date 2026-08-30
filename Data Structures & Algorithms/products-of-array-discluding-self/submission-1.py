class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1]*n
        result = [1]*n

        for leftProd in range(1, n):
            result[leftProd] = nums[leftProd - 1] * result[leftProd - 1]
        for rightProd in range(n-2, -1, -1):
            right[rightProd] = nums[rightProd + 1] * right[rightProd + 1]
        
        for i in range(n):
            result[i] *= right[i]
        return result
        