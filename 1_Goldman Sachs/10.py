'''
Algorithm:-
    * Create min-heap of size K and initialize them with first K elements from the list.
    * Run a loop for the remaining elements and sort the heap
    * if the current element is greater than head of the heap (i.e., heap[0]) then swap
      them. (pop head and and push the current element)
    * Return the min-heap with K largest numbers
'''

def kLargestNumbers(nums, K):
    minHeap = [nums[i] for i in range(K)]
        
    for i in range(K, len(nums)):
        minHeap.sort()
        if nums[i] > minHeap[0]:
            minHeap.pop(0)
            minHeap.append(nums[i])
    
    return minHeap
    
print(kLargestNumbers([3,2,13,1,20,4,15,5,6], 3))