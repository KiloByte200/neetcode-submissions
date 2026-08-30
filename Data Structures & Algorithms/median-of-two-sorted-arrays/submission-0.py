class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        
        left = 0
        right = len(A)

        total = len(A) + len(B)
        half = total // 2

        while left <= right:
            mid = (right - left) // 2 + left

            ARight = A[mid] if mid < len(A) else float("inf")
            ALeft = A[mid-1] if mid > 0 else float("-inf")

            Bmid = half - mid
            BRight = B[Bmid] if Bmid < len(B) else float("inf")
            BLeft = B[Bmid-1] if Bmid > 0 else float("-inf")

            if ALeft > BRight:
                right = mid - 1
            elif BLeft > ARight:
                left = mid + 1
            else:
                if total % 2 == 0:
                    return (max(BLeft, ALeft) + min(BRight, ARight)) / 2
                return min(ARight, BRight)

        
        