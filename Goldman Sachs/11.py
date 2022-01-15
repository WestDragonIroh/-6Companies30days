#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        s = set(arr)
        a = sum(arr)-sum(s)
        b = abs(sum(s)-n*(n+1)//2)
        return a,b
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends