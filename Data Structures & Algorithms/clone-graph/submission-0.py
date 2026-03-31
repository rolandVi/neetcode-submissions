"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self) -> None:
        self.seen = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node.val in self.seen:
            return self.seen[node.val]

        newNode = Node(node.val)
        self.seen[node.val] = newNode

        for nei in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(nei))


        return newNode