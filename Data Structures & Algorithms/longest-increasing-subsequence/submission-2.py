class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        memo = {}

        def LSS(index:int, prev_index:int) -> int:          
            if index >= n:
                return 0

            if (index, prev_index) in memo:
                return memo[(index, prev_index)]
            
            memo[(index, prev_index)] = LSS(index+1, prev_index)
            if prev_index == -1 or nums[index] > nums[prev_index]:
                memo[(index, prev_index)] = max(memo[(index, prev_index)], 1 + LSS(index+1, index))

            return memo[(index, prev_index)]
            
        
        return LSS(0, -1)
            
        