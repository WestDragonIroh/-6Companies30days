#User function Template for python3

class Solution:
    def minSteps(self, D):
        # code here
        N = int(((1+8*D)**.5-1)/2)
        L = N*(N+1)//2
        if L == D:
            return N
        if (L + N + 1 - D) % 2 == 0:
            return N + 1
        return N + 3 - N % 2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        D = int(input())
        
        ob = Solution()
        print(ob.minSteps(D))
# } Driver Code Ends