class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 ={}
        for i in s :
            dict1[i] = dict1.get(i,0)+1
        for j in t:
            if j in dict1:
                if dict1[j] == 0:
                    return False
                else:
                    dict1[j]-=1
            else:
                return False
                break
        
        return True