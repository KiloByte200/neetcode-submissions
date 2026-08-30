class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        length = 0

        for num in nums:
            
            if (num - 1) in seen:
               continue
            
            i = 1
            while (num + i) in seen: 
                i += 1
            length = max(length, i)
        return length