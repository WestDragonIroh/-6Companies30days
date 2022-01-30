class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        lst = []
        visited = set()
        path = set()
        for c1,c2 in prerequisites:
            adj[c2].append(c1)
        for c in range(numCourses):
            if not self.top(c, adj, visited, lst,path):
                return []
        return lst[::-1]
    
    def top(self,node, adj, visited, lst,path):
        if node in path:
            return False
        if node in visited:
            return True
        path.add(node)
        visited.add(node)
        for c in adj[node]:
            if not self.top(c,adj,visited, lst,path):
                return False
        lst.append(node)
        path.remove(node)
        return True