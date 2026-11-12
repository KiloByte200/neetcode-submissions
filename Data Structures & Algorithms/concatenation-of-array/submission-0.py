class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # i -> n-1 ... 0, -1 ... -n+1
        result = []
        for i in range(-len(nums), len(nums)):
            result.append(nums[i])
        
        return result
        