#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        def decode(i):
            ans = ""
            while i < len(s) and s[i] != ']':
                while i < len(s) and s[i].isalpha():
                    ans += s[i]
                    i += 1
                if i >= len(s) or s[i] == ']': continue
                n = ""
                while i < len(s) and s[i].isdigit():
                    n += s[i]
                    i += 1
                tmp, i = decode(i+1)
                ans += tmp * int(n)
            return (ans, i+1)
        return decode(0)[0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends