#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		sm = sum(arr)
        dp = [[0 for i in range(sm + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for j in range(1, sm + 1):
            dp[0][j] = False
        for i in range(1, n + 1):
            for j in range(1, sm + 1):
                dp[i][j] = dp[i - 1][j]
                if arr[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - arr[i - 1]]
        diff = float('inf')
        for j in range(sm//2, -1, -1):
            if dp[n][j]:
                diff = sm - (2 * j)
                break
        return diff

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends