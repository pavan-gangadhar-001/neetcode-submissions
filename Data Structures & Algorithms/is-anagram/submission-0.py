class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s :
            if i in sdict.keys():
                sdict[i] +=1
            else:
                sdict[i] = 1
        for j in t:
            if j in tdict.keys():
                tdict[j] +=1
            else:
                tdict[j] = 1
        skeys = sorted(sdict.keys())
        tkeys = sorted(tdict.keys())
        if skeys != tkeys:
            return False
        if len(skeys) != len(tkeys):
            return False
        for i in skeys:
            if sdict[i] != tdict[i]:
                return False
        return True