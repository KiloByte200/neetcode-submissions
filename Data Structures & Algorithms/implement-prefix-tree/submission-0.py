
class PrefixTree:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        trie = self.root
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie["#"] = None # used to mark the end of a word


    def search(self, word: str) -> bool:
        trie = self.root
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]

        return "#" in trie
        

    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True
        
        