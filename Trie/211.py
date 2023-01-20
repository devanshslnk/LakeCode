class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.head=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.head
        for idx,val in enumerate(word):
            
            if(curr.children.get(val)==None):
                curr.children[val]=TrieNode()
            curr=curr.children[val]
        curr.isEnd=True
        

    def search(self, word: str) -> bool:
        stack=[]
        stack.append((self.head,0))

        while(stack):
            node,counter=stack.pop(0)
            if(counter>=len(word)):
                if(node.isEnd):
                    return True
                continue

            if(word[counter]=='.'):
                for key,value in node.children.items():


                        stack.append((value,counter+1))
            else:
                if(node.children.get(word[counter])!=None):
                    stack.append((node.children[word[counter]],counter+1))

        return False


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
