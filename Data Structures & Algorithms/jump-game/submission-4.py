class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        farthest = 0

        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(i + nums[i], farthest)
        
        return farthest >= n - 1
        
        