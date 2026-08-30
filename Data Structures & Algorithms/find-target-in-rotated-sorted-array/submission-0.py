class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (end - start) // 2 + start

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[end]:  # right side sorted
                if nums[mid] < target <= nums[end]:
                    # target is inside sorted right half
                    start = mid + 1
                else:
                    # target is not inside sorted right half
                    end = mid - 1
            else: # left side sorted
                if nums[start] <= target < nums[mid]:
                    #target in left half inclusive of start and mid
                    end = mid - 1
                else: # not in left half or inclusive of mid
                    start = mid + 1
        return -1

        