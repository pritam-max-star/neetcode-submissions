class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" + s
        return encoded_s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)          # find the next #
            length = int(s[i:j])         # extract the length
            result.append(s[j+1:j+1+length])  # extract the string
            i = j + 1 + length
        return result

        
