class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        best_left = 0
        best_right = 0


        # odd loop
        for i in range(n):
            left = i
            right = i

            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                
                if (best_right - best_left) < (right - left):
                    best_left = left
                    best_right = right
                    
                left -=1
                right +=1
        
            # even loop

            left = i-1
            right = i

            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                
                if (best_right - best_left) < (right - left):
                    best_left = left
                    best_right = right
                left -=1
                right +=1
        
        return s[best_left:best_right+1]

        