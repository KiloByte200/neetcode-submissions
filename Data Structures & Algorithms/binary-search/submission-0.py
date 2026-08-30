class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        mid = n // 2
        end = n - 1


        while start < end:

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
            mid = (end - start) // 2 + start
        
        return mid if nums[mid] == target else -1