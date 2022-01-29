#User function Template for python3

class Solution:
    def isValid(self, mat):
        # code here
        row, col, block = set(), set(), set()
        for i in range(9):
            for j in range(9):
                if mat[i][j] != 0:
                    r_key = (i, mat[i][j])
                    c_key = (j, mat[i][j])
                    b_key = (i//3, j//3, mat[i][j])
                    
                    if (r_key in row) or (c_key in col) or (b_key in block):
                        return 0
                    
                    row.add(r_key)
                    col.add(c_key)
                    block.add(b_key)
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends