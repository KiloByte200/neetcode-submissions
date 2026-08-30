from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        connections = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                cand = word[:i] + "*" + word[i+1:]

                connections[cand].append(word)
        
        queue = deque([beginWord])
        visited = set()

        count = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                
                if word in visited:
                    continue

                visited.add(word)

                if word == endWord:
                    return count

                for i in range(len(word)):
                    cand = word[:i] + "*" + word[i+1:]

                    queue.extend(connections[cand])
            
            count += 1

        return 0
