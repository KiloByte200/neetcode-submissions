class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        trie = self.root
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie["#"] = None # used to mark the end of a word
        

    def search(self, word: str) -> bool:
        trie = self.root

        def looseSearch(start: int, node: dict) -> bool:
            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    for val in node.keys():
                        if val == "#":
                            continue

                        temp = node
                        node = node[val]

                        if looseSearch(i+1, node):
                            return True
                        node = temp
                    return False
     
                elif c not in node:
                    return False
                node = node[c]
            return "#" in node
        
        return looseSearch(0, trie)



        
        
        
