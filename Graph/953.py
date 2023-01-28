class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def check(word1,word2,hmap):
            for i in range(min(len(word1),len(word2))):
                letter1,letter2=word1[i],word2[i]
                if(hmap[letter1]<hmap[letter2]):
                    return True
                elif(hmap[letter1]>hmap[letter2]):
                    return False
            return len(word1)<=len(word2)
        def solve():
            hmap={value:index for index,value in enumerate(order)}
            for i in range(len(words)):
                for j in range(i+1,len(words)):
                    if(not check(words[i],words[j],hmap)):
                        return False
            return True
        return solve()

    # Time Complexity O(n^2) Space Complexty O(n)
