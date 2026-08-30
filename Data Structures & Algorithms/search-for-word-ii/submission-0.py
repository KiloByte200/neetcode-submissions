class Trie:
    def __init__(self):
        self.root = {}
    
    def convertToTrie(self, words:List[str]):

        
        for word in words:
            node = self.root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = word
        
        return self.root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        result = []

        trie = Trie()
        trie = trie.convertToTrie(words)

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1),   # right
        ]

        def backtrack(node: Trie, row: int, col: int) -> None:
            if "#" in node and node["#"] not in result:
                result.append(node["#"])
                
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    new_row < len(board) and new_col < len(board[new_row]) and
                    0 <= new_row and 0 <= new_col and
                    board[new_row][new_col] != "#" and
                    board[new_row][new_col] in node
                    ):
                        temp = board[new_row][new_col]
                        board[new_row][new_col] = "#"

                        backtrack(node[temp], new_row, new_col)
                        
                        
                        board[new_row][new_col] = temp
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                item = board[row][col]
                if item in trie:

                    board[row][col] = "#"
                    backtrack(trie[item], row, col)

                    board[row][col] = item
        return result

        
        