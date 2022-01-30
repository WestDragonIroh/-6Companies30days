class Solution:
	def isWordExist(self, board, word):
		#Code here
		h, w = len(board), len(board[0])
        def dfs_search(idx: int, x: int, y: int) -> bool:
            if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
                return False
            if idx == len(word) - 1:
                return True
            cur = board[y][x]
            board[y][x] = '#'
            found = dfs_search(idx + 1, x + 1, y) or dfs_search(idx + 1, x - 1, y) or dfs_search(idx + 1, x, y + 1) or dfs_search(idx + 1, x, y - 1)
            board[y][x] = cur
            return found
        for i in range(w):
            for j in range(h):
                if dfs_search(0, i, j):
                    return True
        return False

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n, m = map(int, input().split())
		board = []
		for i in range(n):
			a = list(input().strip().split())
			b = []
			for j in range(m):
				b.append(a[j][0])
			board.append(b)
		word = input().strip()
		obj = Solution()
		ans = obj.isWordExist(board, word)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends