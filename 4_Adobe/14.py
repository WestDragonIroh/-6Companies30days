#User function Template for python3
import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        heap = []
        maximum = -float('inf')
        for i, arr in enumerate(KSortedArray):
            heapq.heappush(heap, (arr[0], i, 0))
            maximum = max(maximum, arr[0])
        heapq.heapify(heap)
        diff = maximum - heap[0][0]
        res = [heap[0][0], maximum]
        while True:
            minimum, i, j = heapq.heappop(heap)
            if diff > maximum - minimum:
                diff = maximum - minimum
                res = [minimum, maximum]
            if j+1 >= len(KSortedArray[i]):
                break
            num = KSortedArray[i][j+1]
            maximum = max(maximum, num)
            heapq.heappush(heap, (num, i, j+1))
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends