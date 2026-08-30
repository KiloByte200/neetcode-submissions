class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        leftMax = height[0]
        rightMax = height[n-1]

        left = 0
        right = n - 1 

        totalWater = 0
        
        while left < right:
            if height[left] <= height[right]:
                leftMax = max(leftMax, height[left])
                boundary = max(leftMax - height[left], 0)
                totalWater += boundary
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                boundary = max(rightMax - height[right], 0)
                totalWater += boundary
                right -= 1

        
        return totalWater