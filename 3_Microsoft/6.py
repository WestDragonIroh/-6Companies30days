#User function Template for python3


class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        comb = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        def check(i, lst):
            if len(lst) == N:
                res.append("".join(lst))
                return
            
            temp = comb[a[i]]
            for t in temp:
                lst.append(t)
                check(i+1, lst)
                lst.pop()
        
        res = []
        check(0, [])
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends