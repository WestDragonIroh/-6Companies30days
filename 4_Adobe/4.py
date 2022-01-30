# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        total_sum = sum(arr)
        if total_sum & 1:
            return False
        half_sum = total_sum // 2
        dp = [True] + [False]*half_sum
        for num in arr:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[half_sum]

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends