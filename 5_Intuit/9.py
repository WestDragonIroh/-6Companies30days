class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        res = []
        m, n = len(heights), len(heights[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        p_visited = [[False]*n for _ in range(m)]
        a_visited = [[False]*n for _ in range(m)]
        
        def check(x,y):
            return x >= 0 and x < m and y >= 0 and y < n
        
        def dfs(i, j, visited):
            visited[i][j] = True
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if check(ni, nj) and not visited[ni][nj] and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)
        
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m-1, j, a_visited)
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        return res