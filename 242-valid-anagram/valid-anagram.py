class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 ={}
        for i in s :
            dict1[i] = dict1.get(i,0)+1
        for j in t:
            if j not in dict1 or dict1[j] == 0:
                return False
            dict1[j]-=1
        return True