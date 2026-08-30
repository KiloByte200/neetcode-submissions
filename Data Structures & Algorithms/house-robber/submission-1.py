class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n


        def backtrack(house: int) -> int:
            if house >= n:
                return 0
            
            if memo[house] != -1:
                return memo[house]
            
            memo[house] = nums[house] + max(backtrack(house+2), backtrack(house + 3))

            return memo[house]
        
        return max(backtrack(0), backtrack(1))
        