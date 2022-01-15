#User function Template for python3

class Solution:
	def canPair(self, nuns, k):
		# Code here
		A = dict([(p,0) for p in range(k)])
        for x in  nuns:
            A [x % k] += 1 
        
        if A[0] % 2 != 0:
            return False
        for p in range(1,k):
            if p != (k-p):
                if A[p] != A[k-p]:
                    return False
            else:
                if A[p] % 2 != 0:
                    return False
        
        
        return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends