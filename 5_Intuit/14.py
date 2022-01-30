class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = collections.deque([(i, j, 0) for i in range(n) for j in range(n) if grid[i][j]])
        if len(queue) == n * n or len(queue) == 0:
            return -1
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        seen = set()
        while queue:
            x, y, step = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in seen:
                    queue.append((nx, ny, step+1))
                    seen.add((nx, ny))
        return step