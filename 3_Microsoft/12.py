#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        arr.sort()
        n = len(arr)
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                l, r = j + 1, n - 1
                remain = k - arr[i] - arr[j]
                while l < r:
                    if arr[l] + arr[r] == remain:
                        ans.add((arr[i], arr[j], arr[l], arr[r]))
                        l += 1
                        r -= 1
                    elif arr[l] + arr[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return sorted(ans)

#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends