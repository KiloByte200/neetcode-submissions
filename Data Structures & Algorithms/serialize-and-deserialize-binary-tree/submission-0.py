# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized_buffer = []

        def encode_node(node: Optional[TreeNode]) -> None:
            serialized_buffer.append("$")
            if not node:
                serialized_buffer.append("#")
                return
            
            serialized_buffer.append(str(node.val))
            encode_node(node.left)
            encode_node(node.right)


        encode_node(root)
        return ''.join(serialized_buffer)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder_list = data.split("$")
        n = len(preorder_list)
        count = 1

        def dfs() -> Optional[TreeNode]:
            nonlocal count

            if count >= n:
                return
            
            node_val = preorder_list[count]
            count += 1

            if node_val == "#":
                return
            
            node = TreeNode(int(node_val), dfs(), dfs())
            return node

        return dfs()

            
