#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		hmap = {}
        q = []
        res = []
        for i in range(len(A)):
            if A[i] not in hmap:
                hmap[A[i]] = 1
            else:
                hmap[A[i]] += 1
            q.append(A[i])
            while len(q) > 0:
                if hmap[q[0]] and hmap[q[0]] > 1:
                    q.pop(0)
                else:
                    break
            if len(q) < 1:
                res.append('#')
            else:
                res.append(q[0])
        return ''.join(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends