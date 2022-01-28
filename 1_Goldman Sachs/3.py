#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        count, curr, start = 0, 1, 0

        for i in range(len(a)):
            curr *= a[i]
            while start < i and curr >= k:
                curr //= a[start]
                start += 1            
            if curr < k: 
                count += (i-start) + 1

        return count
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends