class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s)) # --> [5, 5]

        for sz in sizes:
            res += str(sz) + "," # --> "5,5"
        res += "#" # --> "5,5#"
        
        for s in strs:
            res += s # -- "5,5#helloworld"
        
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes, res, i = [], [], 0

        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur)) # --> [5, 5]
            i += 1
        i += 1 # moves it past the "#"

        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz

        return res

        




        
        

