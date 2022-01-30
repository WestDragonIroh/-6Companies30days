#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        sign = 1
        i = 0
        res = 0
        if string[i] == '-':
            sign = -1
            i += 1
        while i < len(string):
            if not (ord(string[i])-ord('0') >= 0 and ord(string[i])-ord('0') <= 9):
                return -1
            res = res*10 + (ord(string[i])-ord('0'))
            i += 1
        return res*sign

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends