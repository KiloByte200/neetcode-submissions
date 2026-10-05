class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)

        memo = [[-1] * len_t for _ in range(len_s)]

        def dp(index1: int, index2: int) -> int:
            if index2 >= len_t:
                return 1
            
            if index1 >= len_s:
                return 0
            
            if memo[index1][index2] != -1:
                return memo[index1][index2]
            
            # keep and move
            keep = 0
            if s[index1] == t[index2]:
                keep = dp(index1+1, index2+1)
            
            skip = dp(index1+1, index2)

            memo[index1][index2] = keep + skip
            return memo[index1][index2]
        
        return dp(0, 0)

