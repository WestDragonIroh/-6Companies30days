#User function Template for python3
class Solution:
	def numOfWays(self, n, x):
		# code here
		dp = [0 for i in range(n+1)]
        dp[0] = 1
        MOD = 10**9 + 7
        for i in range(1, n+1):
            for j in range(n, i-1, -1):
                y = i**x
                if j >= y:
                    dp[j] = (dp[j] + dp[j-y]) % MOD
        return dp[n]


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,x = input().split()
		n=int(n)
		x=int(x)
		ob = Solution();
		print(ob.numOfWays(n, x))

# } Driver Code Ends