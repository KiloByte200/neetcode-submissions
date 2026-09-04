class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [-1] * n

        def backtrack(start: int):
            if start >= n:
                return 1

            if s[start] == "0":
                return 0

            memo = 0

            if dp[start] == -1:
                memo = backtrack(start+1) 

                if start < n - 1 and 1 <= int(s[start: start+2]) <= 26:
                    memo += backtrack(start+2)
                
                dp[start] = memo
            
            return dp[start]
        
        return backtrack(0)
            
        