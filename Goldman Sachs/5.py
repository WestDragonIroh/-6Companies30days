#User function Template for python3
class Solution:
	def getNthUglyNo(self,n):
		# code here
		arr = [0]*n             
        arr[0] = 1              
        x2 = x3 = x5 = 0        

        mul2,mul3,mul5 = 2,3,5

        for i in range(1,n):
            arr[i] = min(mul2, mul3, mul5)
            if arr[i] == mul2:                          
                x2+=1                                    
                mul2 = arr[x2] * 2                      
            if arr[i] == mul3:                           
                x3+=1
                mul3 = arr[x3] * 3
            if arr[i] == mul5:
                x5+=1
                mul5 = arr[x5] * 5
        return arr[-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends