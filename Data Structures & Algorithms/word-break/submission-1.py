class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {} # key-> word so far , value -> true or false?

        def validBreak(word:str) -> bool:
            if word == s:
                return True
            
            if not s.startswith(word):
                return False
            
            if word in memo:
                return memo[word]

            memo[word] = False
            for cand in wordDict:
                if validBreak(word+cand):
                    memo[word] = True
                    break
            
            return memo[word]
        
        return validBreak("")
