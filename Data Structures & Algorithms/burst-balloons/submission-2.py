class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = [[-1] * len(nums) for _ in range(len(nums))]

        def dp(left: int, right: int) -> int:
            if right - left < 2:
                return 0
            
            if memo[right][left] != -1:
                return memo[right][left]

            max_so_far = 0
            for k in range(left + 1, right):
                max_so_far = max(
                    max_so_far,
                    (nums[left] * nums[k] * nums[right])
                    + dp(left, k) + dp(k, right))
            
            memo[right][left] = max_so_far
            
            return max_so_far
        
        return dp(0, len(nums) - 1)
        