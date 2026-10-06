class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        memo = [[-1] * n2 for _ in range(n1)]

        def operations(index1: int, index2: int) -> int:
          
            if index1 >= n1:
                return n2 - index2
            
            if index2 >= n2:
                return n1 - index1

            if memo[index1][index2] != -1:
                return memo[index1][index2]

            if word1[index1] == word2[index2]:
                memo[index1][index2] = operations(index1+1, index2+1)
                return memo[index1][index2]
            
            
            #insert
            insert = 1 + operations(index1, index2+1)

            #delete char
            delete = 1 + operations(index1+1, index2)

            #replace
            replace = 1 + operations(index1+1, index2+1)

            memo[index1][index2] = min(insert, delete, replace)

            return memo[index1][index2]
        
        return operations(0, 0)

        