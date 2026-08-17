class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return "ö"
        ret = []
        for i in range(len(strs)):
            newChar = ""
            for character in range(len(strs[i])):

                newChar = newChar + chr(ord(strs[i][character]) + character)

            ret.append(newChar + chr(0))
        return chr(0).join(ret)

    def decode(self, s: str) -> List[str]:
        if(s == "ö"):
            return []
        strs = s.split(chr(0))
        ret = []
        for i in range(0,len(strs),2):
            newChar = ""
            for character in range(len(strs[i])):

                newChar = newChar + chr(ord(strs[i][character]) - character)

            ret.append(newChar)
        return ret