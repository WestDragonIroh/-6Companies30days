class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		#Code here
		m, n = len(grid), len(grid[0])
		def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i, j+1) + dfs(i+1, j+1) + dfs(i+1, j) + dfs(i+1, j-1) + dfs(i, j-1) + dfs(i-1, j-1) + dfs(i-1, j) + dfs(i-1, j+1)
            return 0
        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0


#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.findMaxArea(grid)
		print(ans)

# } Driver Code Ends