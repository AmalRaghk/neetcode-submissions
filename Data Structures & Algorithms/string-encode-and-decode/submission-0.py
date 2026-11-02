class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            start_of_string = j + 1
            end_of_string = start_of_string + length
            res.append(s[start_of_string:end_of_string])            
            i = end_of_string
            
        return res