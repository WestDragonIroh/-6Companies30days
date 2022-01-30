"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row,col,n):
            total = 0             
            for c in grid[row:row+n]:
                total += sum(c[col:col+n])
            if n == 1 or total in [0,n*n]:
                return Node(grid[row][col],1,None,None,None,None)
            n = n//2
            topLeft = dfs(row,col,n)
            topRight = dfs(row,col+n,n)
            bottomLeft = dfs(row+n,col,n)
            bottomRight = dfs(row+n,col+n,n)
            root = Node(0,0,topLeft,topRight,bottomLeft,bottomRight)
            return root
        
        n = len(grid)
        return dfs(0,0,n)