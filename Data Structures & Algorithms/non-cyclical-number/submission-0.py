
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        temp = n

        while temp != 1:
            total = 0
            while temp != 0:
                total += (temp % 10)**2
                temp //= 10
            
            if total in seen:
                return False
            
            seen.add(total)
            temp = total
        
        return True