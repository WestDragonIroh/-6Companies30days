#User function Template for python3

class Solution:
    def maxProfit(self, k, n, prices):
        # code here
        if not prices:
            return 0 
        
        K = k+1
        
        if k>=n//2:
            maxProf = 0
            buy = prices[0]
            for i in range(1, n):
                maxProf +=max(0, prices[i]-prices[i-1])
            return maxProf
                
        dp =[[0]*n for _ in range(K)]
        
        for i in range(1, K):
            buy = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j], prices[j]+buy, dp[i][j-1])
                buy = max(buy, -prices[j]+dp[i-1][j-1])
        return dp[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends