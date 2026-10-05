class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring=""
        for i in s:
            if i.isalpha() or i.isdigit():
                newstring = newstring+i

        newstring = newstring.lower()
        l = len(newstring)
        ld2 = int(l/2)

        if l%2==1:
            return newstring[0:ld2] == newstring[ld2+1:l][::-1]
        return newstring[0:ld2] == (newstring[ld2:l])[::-1]