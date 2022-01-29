#User function Template for python3

def rotate(matrix): 
    #code here
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = tmp

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends