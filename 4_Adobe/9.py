#User function Template for python3

class Solution:
    def nextPalin(self,N):
        #code here
        n = len(N)
        res = list(N)
        mid = n//2 - 1
        pos = -1
        for i in range(mid, 0, -1):
            if res[i-1] < res[i]: 
                pos = i-1
                break
        
        if pos == -1: 
            return "-1"
        
        numPos = -1;
        for i in range(pos+1, mid+1):
            if res[i] > res[pos]:
               if numPos == -1:
                   numPos = i
               else:
                   if res[i] < res[numPos]:
                       numPos = i
    
        temp = res[pos]
        res[pos] = res[numPos]
        res[numPos] = temp

        res[pos+1:mid+1] = sorted(res[pos+1:mid+1])
        i = 0
        j = n-1
        while i <= mid:
            res[j] = res[i]
            i += 1
            j -= 1
        return ''.join(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
# } Driver Code Ends