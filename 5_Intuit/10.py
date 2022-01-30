class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            seen[i] = 1
            for j in range(n):
                if isConnected[i][j] == 1 and seen[j] == 0:
                    dfs(j)
            
        n = len(isConnected)
        res = 0
        seen = [0]*n
        for i in range(n):
            if seen[i] == 0:
                dfs(i)
                res += 1
        return res