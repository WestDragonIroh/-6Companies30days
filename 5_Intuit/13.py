class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        for row in grid:
            cnt = 0
            for i in range(n-1, -1, -1):
                if row[i] == 1:
                    break
                cnt += 1
            zeros.append(cnt)
        
        res = 0
        for i in range(n):
            target = n - 1 - i
            if zeros[i] >= target:
                continue
            flag = False
            for j in range(i+1, n):
                if zeros[j] >= target:
                    flag = True
                    res += j - i
                    zeros[i+1:j+1] = zeros[i:j]
                    break
            if not flag:
                return -1
        
        return res