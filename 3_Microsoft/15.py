#User function Template for python3

#User function Template for python3
class graph:
    def __init__(self, k):
        self.matrix = [ [False for _ in range(k)] for _ in range(k) ]
        self.ancestors = [0 for _ in range(k)]
        self.index = {}
        self.next_index = 0
        self.characters = ''
    
    def add_char(self, char):
        if char in self.index:
            return
        self.index[char] = self.next_index
        self.next_index += 1
        self.characters += char
    
    def add_edge(self, first, second):
        i1 = self.index[first]
        i2 = self.index[second]
        if self.matrix[i1][i2]:
            return
        self.ancestors[i2] += 1
        self.matrix[i1][i2] = True
    
    def dfs(self, location, order):
        if self.ancestors[location]>1:
            self.ancestors[location] -= 1
            return
        
        order.append(self.characters[location])
        
        for i in range(len(self.matrix)):
            if self.matrix[location][i]:
                self.dfs(i,order)
    
    def topo_sort(self):
        order = []
        for i in range(len(self.matrix)):
            if self.ancestors[i] == 0:
                self.dfs(i,order)
        return order

class Solution:
    def findOrder(self,dict, N, K):
    # code here
        g = graph(k)
        for c in dict[0]:
            g.add_char(c)
        
        for i in range(1,n):
            for c in dict[i]:
                g.add_char(c)
            
            length = min( len(dict[i]) , len(dict[i-1]) )
            for j in range(length):
                if dict[i-1][j] != dict[i][j]:
                   g.add_edge( dict[i-1][j] , dict[i][j] )
                   break
        
        lst = g.topo_sort()
        order = ''
        for c in lst:
            order += c
        return order


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends