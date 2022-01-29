#User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def all_words(self, prefix):
        if self.isEnd:
            yield prefix
        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for letter in word:
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter] = node
            curr = node
        curr.isEnd = True
            
    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  
        yield from cur.all_words(prefix)

class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        t = Trie()
        for i in range(n):
            t.add(contact[i])
        words = []
        for i in range(len(s)):
            curr = list(t.all_words_beginning_with_prefix(s[:i+1]))
            if len(curr) > 0:
                words.append(curr)
        for i in range(len(s) - len(words)):
            words.append(['0'])
        return words

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends