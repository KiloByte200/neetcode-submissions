class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        mem = {}

        def sumWays(running_total: int, index: int) -> int:
            if running_total == target and index == n:
                return 1

            if index >= n:
                return 0
            
            if (index, running_total) in mem:
                return mem[(index, running_total)]

            # add
            add = sumWays(running_total + nums[index], index+1)
            # subtract
            subtract = sumWays(running_total - nums[index], index+1)

            mem[(index, running_total)] = add + subtract

            return mem[(index, running_total)]
        
        return sumWays(0, 0)
        