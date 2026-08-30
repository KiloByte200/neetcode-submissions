class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        # Create s1 freq list
        s1_freq = [0] * 26
        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1

        # Inital s2_freq:
        s2_freq = [0] * 26
        for c in s2[0: n1]:
            s2_freq[ord(c) - ord('a')] += 1
        
        if s1_freq == s2_freq:
                return True
        
        for i in range(0, n2 - n1):
            s2_freq[ord(s2[i])-ord('a')] -= 1
            s2_freq[ord(s2[i+n1])-ord('a')] += 1
            
            if s1_freq == s2_freq:
                return True
            
        
        return False
        