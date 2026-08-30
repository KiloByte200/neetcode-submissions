class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start < end:
            mid = start + (end - start) // 2

            cand_h = 0
            for pile in piles:
                cand_h += (pile + mid - 1) // mid
            
            if cand_h > h:
                start = mid + 1
            else:
                end = mid
        
        return start