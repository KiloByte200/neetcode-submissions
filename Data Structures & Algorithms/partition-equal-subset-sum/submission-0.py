class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        memo = {} # key -> subset 1 or subset 2 -> value true / False
        target = sum(nums)
        total = 0

        if target % 2 == 1:
            return False

        def partition(index:int) -> bool:
            nonlocal total

            if index >= n:
                return total == target // 2

            if (total, index) in memo:
                return memo[(total, index)]

            # two cases -> add num to subset1 or add to subset2

            result1 = partition(index+1)

            total += nums[index]
            result2 = partition(index+1)

            total -= nums[index]

            memo[(total, index)] = result1 or result2

            return memo[(total, index)]
        
        return partition(0)
        