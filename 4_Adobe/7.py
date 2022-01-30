class Solution:
    def maxCoins(self,arr, n):
        # Code here
        cache = {}
        return self.optimal(arr, 0, len(arr) - 1, 'X', cache)
        
    def optimal(self, arr, left, right, player, cache): 
        if left > right:
            return 0
        if (left, right, player) in cache:
            return cache[(left, right, player)]
        if player == 'X': 
            result = max(self.optimal(arr, left + 1, right, 'Y', cache) + arr[left], self.optimal(arr, left, right - 1, 'Y', cache) + arr[right]) 
        else: 
            result = min(self.optimal(arr, left + 1, right, 'X', cache), self.optimal(arr, left, right - 1, 'X', cache)) 
        cache[(left, right, player)] = result 
        return result
 

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends