class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        encodedS = ""
        for s in strs:
            encodedS += str(len(s)) + "#" + s # --> "5#Hello5#World"
        return encodedS

    def decode(self, s: str) -> List[str]:
        res =[]
        i = 0 

        # --> "5#Hello5#World"
        while i < len(s):
            numStr = ''
            while s[i].isdigit():
                numStr += s[i]
                i += 1

            length = int(numStr)
            if s[i] == "#":
                i += 1
                word = s[i : i + length]
                res.append(word)

                i += length
        return res
        
        

