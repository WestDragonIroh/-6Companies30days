class Solution:
    def minSubArrayLen(self, t: int, n: List[int]) -> int:
        r = float('inf')
        s = 0
        l = len(n)
        if l <= 1:
            return 0
        i,j = 0,0
        x = 0
        while i < l and j <l:
            if i == j:
                if n[i] >= t:
                    return 1 
                j += 1
            else:
                s = sum(n[i:j+1])
                if s >= t:
                    r = min(r, j-i+1)
                    i += 1
                    x = 1
                else:
                    j += 1
        if x :
            return r
        else :
            return 0