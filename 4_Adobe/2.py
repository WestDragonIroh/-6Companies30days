#User function Template for python3

class Solution:
    def lengthOfLongestAP(self, A, n):
        # code here
        if n < 3:
            return n
        dp = [{} for _ in range(n)]
        ans = 0
        
        for i in range(n):
            dp[i][0] = 1
            for j in range(i):
                diff = A[i] - A[j]
                
                if diff not in dp[j]:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff] + 1
                    
            ans = max(ans, max(dp[i].values()))
            
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(A, n)
        print(ans)
        tc -= 1

# } Driver Code Ends