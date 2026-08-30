class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        temp = set(nums)
        return len(temp) != len(nums)
        