class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while front < back:
            while not s[front].isalnum() and front < back:
                front += 1
            while not s[back].isalnum() and front < back:
                back -= 1

            if s[front].lower() != s[back].lower():
                return False
            
            front += 1
            back -= 1
        return True        