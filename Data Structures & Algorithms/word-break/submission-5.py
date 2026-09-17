class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {} # key-> word so far at index , value -> true or false?

        def validBreak(start:int) -> bool:

            if start == n:
                return True
            
            if start in memo:
                return memo[start]

            memo[start] = False
            for cand in wordDict:
                if s.startswith(cand, start) and validBreak(start + len(cand)):
                    memo[start] = True
                    break
            
            return memo[start]
        
        return validBreak(0)
