class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            front, back = i + 1, n - 1
            while front < back:
                cand = nums[i] + nums[front] + nums[back]
                
                if cand > 0:
                    back -= 1
                elif cand < 0:
                    front += 1
                else:
                    result.append([nums[i], nums[front], nums[back]])
                    front += 1
                    back -= 1

                    while front < back and nums[front] == nums[front-1]:
                        front += 1
                    while front < back and nums[back] == nums[back+1]:
                        back -= 1
        return result

        