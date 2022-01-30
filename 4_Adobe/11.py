#User function Template for python3

class Solution:

    def amendSentence(self, s):

        # code here
        res = ''
        for i in range(len(s)):
            if s[i] >= 'A' and s[i] <= 'Z':
                temp = chr(ord(s[i]) + 32)
                if i != 0:
                    res += ' '
                res += temp
            else:
                res += s[i]
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.amendSentence(s))
        

# } Driver Code Ends