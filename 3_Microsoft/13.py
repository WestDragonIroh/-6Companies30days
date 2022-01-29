#User function Template for python3

class Solution:
   
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        # code here
        if self.isConnected(V, adj, c, d) == False:
            return 0
        indU = adj[d].index(c)
        indV = adj[c].index(d)
        del adj[c][indV]
        del adj[d][indU]
        res = self.isConnected(V, adj, c, d)
        adj[c].append(d)
        adj[d].append(c)
        if res:
            return 0
        else:
            return 1
            
    def isConnected(self, V, adj, u, v):
        visited = [False] * V
        self.dfs(adj, u, visited)
        if visited[v] == False:
            return False
        return True
        
    def dfs(self, adj, source, visited):
        visited[source] = True
        i = 0
        while i != len(adj[source]):
            if not visited[adj[source][i]]:
                self.dfs(adj, adj[source][i], visited)
            i += 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends