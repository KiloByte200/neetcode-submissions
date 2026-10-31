from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)


        @cache
        def jumps(index:int) -> bool:
            if index >= n - 1:
                return True

            if nums[index] == 0:
                return False

            
            for i in range(nums[index]):
                if jumps(index + i + 1):
                    return True
            
            return False

        return jumps(0)