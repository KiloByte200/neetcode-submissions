class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {} # key-> word so far , value -> true or false?

        def validBreak(start:int) -> bool:
            word = s[start:]
            if word == "":
                return True
            
            if word in memo:
                return memo[word]

            memo[word] = False
            for cand in wordDict:
                if word.startswith(cand) and validBreak(start + len(cand)):
                    memo[word] = True
                    break
            
            return memo[word]
        
        return validBreak(0)
