class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        l = [e.lower() for e in s]
        print(l)
        ln = len(l)
        ele = 0
        while ele < ln:
            print("Len",ele)
            if not l[ele].isalnum() or l[ele] == " ":
                l.pop(ele)
                ln-=1
                continue
            ele+=1
        print(l)
        return l == l[::-1]