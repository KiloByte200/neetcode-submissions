from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Create dictionary called "less_than" -> stores key for a character and a value that is lexicographically less than the key

        # look through words looking at i and i+1.
        # use another loop looking at individual characters
        #   if characters don't match, first word character becomes new key and second character word becomes value
        #   if we don't find an non-matching character and one is longer than the other, we return ""

        # throughout the loop we keep track of the latest letter pushed. We traverse and create a string using that letter and the dictionary. 

        less_than = defaultdict(set)
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            
            n = min(len(word1), len(word2))
            
            for j in range(n):
                if word1[j] != word2[j]:
                    less_than[word1[j]].add(word2[j])
                    break
            else:
                if len(word1) > len(word2):
                    return ""



        visited = set()
        visiting = set()

        result = []

        def dfs(node: str) -> bool:
            if node in visiting:
                return False

            if node in visited:
                return True

            visiting.add(node)
            if node in less_than:
                for cand in less_than[node]:
                    if not dfs(cand):
                        return False
                    
            
            visiting.remove(node)
            visited.add(node)

            result.append(node)
            return True
        
        for word in words:
            for letter in word:
                if not dfs(letter):
                    return ""
        
        return ''.join(result[::-1])

        

