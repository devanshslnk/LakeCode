class Solution:
    def modifyString(self, s: str) -> str:
        arrS=list(s)
        for i in range(len(s)):
            if(arrS[i]=="?"):
                for j in range(97,100):
                    char=chr(j)

                    if(i==0 and i!=len(s)-1):
                        if(arrS[i+1]!=char):
                            arrS[i]=char
                            break
                    elif(i==len(s)-1 and i!=0):
                        # char=chr(j)
                        if(arrS[i-1]!=char):
                            arrS[i]=char
                            break
                    elif(0<i<len(s)-1):
                        if(arrS[i-1]!=char and arrS[i+1]!=char):
                            arrS[i]=char
                            break
                    else:
                        arrS[i]=char
        return "".join(arrS)

    # Time COmplexity O(n) and Space Complexity O(n)

