class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1] * n2 for _ in range(n1)]
        def match(index1: int, index2:int) -> int:
            if n1 <= index1 or n2 <= index2:
                return 0
            
            if dp[index1][index2] != -1:
                return dp[index1][index2]
            
            if text1[index1] == text2[index2]:
                dp[index1][index2] = 1 + match(index1 + 1, index2 + 1)
                return dp[index1][index2]

            # keep looking for letter
            result1 = match(index1+1, index2)

            # cut losses and move on
            result2 = match(index1, index2 + 1)

            dp[index1][index2] = max(result1, result2)
            return dp[index1][index2]
        
        return match(0, 0)
        