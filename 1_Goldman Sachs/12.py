#User function Template for python3

class Solution:
    def squaresInChessBoard(self, N):
         # code here
         return int((N*(N+1)*(2*N+1))/6)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.squaresInChessBoard(N))
# } Driver Code Ends