from collections import defaultdict

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        connections = defaultdict(list)
        remaining_words = set(wordList)

        if endWord not in remaining_words:
            return 0

        remaining_words.discard(beginWord)
        remaining_words.discard(endWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                connections[pattern].append(word)

        begin_frontier = {beginWord}
        end_frontier = {endWord}
        length = 1

        while begin_frontier and end_frontier:

            if len(begin_frontier) > len(end_frontier):
                begin_frontier, end_frontier = end_frontier, begin_frontier
            
            next_frontier = set()

            for _ in range(len(begin_frontier)):
                word = begin_frontier.pop()

                if word in end_frontier:
                    return length

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for neighbor in connections[pattern]:
                        if neighbor in end_frontier:
                            return length+1

                        if neighbor in remaining_words:
                            remaining_words.remove(neighbor)
                            next_frontier.add(neighbor)
            
            begin_frontier = next_frontier

            length += 1


        return 0