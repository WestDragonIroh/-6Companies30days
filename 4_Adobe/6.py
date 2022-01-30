#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        results = []
        stack = []
        stack.append(('', n, n))
        while stack:
            sofar, left, right = stack.pop()
            if left == 0 and right == 0:
                results.append(sofar)
            if left > 0:
                stack.append((sofar + "(", left-1, right))
            if right > left:
                stack.append((sofar + ")", left, right-1))
        return results


#{ 
#  Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends