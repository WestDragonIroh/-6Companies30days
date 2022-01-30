#User function Template for python3
import bisect

class Solution:
    def LISLength(self, v):
        if len(v) == 0:
            return 0
        tail = [0 for i in range(len(v) + 1)]
        length = 1
        tail[0] = v[0]
        for i in range(1, len(v)):
            if v[i] > tail[length-1]:
                tail[length] = v[i]
                length += 1
            else:
                tail[bisect.bisect_left(tail, v[i], 0, length-1)] = v[i]
        return length
        
    def minInsAndDel(self, A, B, N, M):
        # code here 
        hm = dict()
        for i in range(M):
            hm[B[i]] = i 
        res = []
        for i in range(N):
            if A[i] in hm:
                res.append(hm[A[i]])
        ans = (N-self.LISLength(res)) + (M-self.LISLength(res))
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minInsAndDel(A,B,N,M))
# } Driver Code Ends