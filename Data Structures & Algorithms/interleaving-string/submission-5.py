class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n3 != n1 + n2:
            return False

        memo = [[-1] * (n2+1) for _ in range(n1+1)]

        def interleave(index1: int, index2: int) -> bool:
            if index1 >= n1 and index2 >= n2:
                return True
            
            if memo[index1][index2] != -1:
                return bool(memo[index1][index2])

            if index1 < n1 and s1[index1] == s3[index1+index2]:
                if interleave(index1+1, index2):
                    memo[index1][index2] = 1
                    return True

            if index2 < n2 and s2[index2] == s3[index1+index2]:
                if interleave(index1, index2+1):
                    memo[index1][index2] = 1
                    return True
            
            memo[index1][index2] = 0
            return False
        
        return interleave(0, 0)

        
        