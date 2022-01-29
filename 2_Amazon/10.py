#User function Template for python3
class Solution:

	def matchPairs(self,nuts, bolts, n):
		# code here
		self.quickSort(nuts, bolts, 0, n-1)
		
	def partition(self, arr, low, high, pivot):
        i, j = low, low
        while j < high:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            elif arr[j] == pivot:
                arr[j], arr[high] = arr[high], arr[j]
                j -= 1
            j += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
    
    def quickSort(self, nuts, bolts, low, high):
        if low < high:
            pivot = self.partition(nuts, low, high, bolts[high])
            self.partition(bolts, low, high, nuts[pivot])
            self.quickSort(nuts, bolts, low, pivot-1)
            self.quickSort(nuts, bolts, pivot+1, high)

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends