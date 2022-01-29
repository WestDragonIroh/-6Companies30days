#User function Template for python3

class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        def dfs(i):
            lst[i] = 1
            if i in graph:
                for j in graph[i]:
                    if lst[j] == 0:
                        if not dfs(j):
                            return False
                    elif lst[j] == 1:
                        return False
            lst[i] = 2
            return True
                            
        graph = {}
        for pair in prerequisites:
            if pair[1] in graph:
                graph[pair[1]].add(pair[0])
            else:
                graph[pair[1]] = set([pair[0]])			
        lst = [0]*N
        for i in range(N):
            if lst[i] == 0:
                if not dfs(i):
                    return False
        return True

    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends