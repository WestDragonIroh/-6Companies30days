#User function Template for python3

class Solution:
    def kvowelwords(self, N,K):
		# code here
		i, j = 0, 0
        MOD = 1000000007
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        res = 1
        for i in range(1, N + 1):
            dp[i][0] = res * 21
            dp[i][0] %= MOD
            res = dp[i][0]
            for j in range(1, K + 1):
                if j > i:
                    dp[i][j] = 0
                elif j == i:
                    dp[i][j] = (5**i) % MOD
                else:
                    dp[i][j] = dp[i - 1][j - 1] * 5
                dp[i][j] %= MOD
                res += dp[i][j]
                res %= MOD
        return res




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = map(int,input().split())
		ob = Solution()
		ans = ob.kvowelwords(N,K)
		print(ans)
# } Driver Code Ends