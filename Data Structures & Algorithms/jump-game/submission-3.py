class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        seen = [False] * n
        seen[0] = True

        for i in range(len(nums)):
            
            jumpCount = min(nums[i], n - 1 - i)
            while jumpCount > 0 and n > (i + jumpCount):
                seen[i + jumpCount] = seen[i + jumpCount] or seen[i]
                jumpCount -= 1
        
        return seen[n-1]
        
        