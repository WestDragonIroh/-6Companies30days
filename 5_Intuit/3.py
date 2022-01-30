# your task is to complete this function
# function should return the missing number
# else return -1
import math
MAX_DIGITS = 6

def getValue(s, i, m):
    if i + m > len(s):
        return -1
    value = 0
    for j in range(m):
        c = (ord(s[i + j]) - ord('0'))
        if c < 0 or c > 9:
            return -1
        value = value * 10 + c
    return value

def missingNumber(string):
    # Code here
    for m in range(1, MAX_DIGITS + 1):
        n = getValue(string, 0, m)
        if n == -1:
            break
        missingNo = -1
        fail = False
        i = m
        while i != len(string):
            if missingNo == -1 and getValue(string, i, 1 + int(math.log10(n + 2))) == n + 2:
                missingNo = n + 1
                n += 2
            elif getValue(string, i, 1 + int(math.log10(n + 1))) == n + 1:
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))
        if not fail:
            return missingNo
    return -1

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(missingNumber(string))
# Contributed by: Harshit Sidhwa

# } Driver Code Ends