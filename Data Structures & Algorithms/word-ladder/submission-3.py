from collections import defaultdict, deque

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        connections = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                connections[pattern].append(word)

        queue = deque([beginWord])
        visited = {beginWord}
        length = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return length

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for neighbor in connections[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                    connections[pattern] = []

            length += 1

        return 0