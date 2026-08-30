class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        curr = []

        def isPalindrome(s: str) -> bool:
            n = len(s)
            for i in range(n//2):
                if s[i] != s[n-i-1]:
                    return False
            return True
        
        def backtrack(s: str):
            if s == "":
                result.append(curr.copy())
                return

            for i in range(1, len(s)+1):
                if isPalindrome(s[0:i]):
                    curr.append(s[0:i])
                    backtrack(s[i:])
                    curr.pop()
        
        backtrack(s)
        return result
            
        
        