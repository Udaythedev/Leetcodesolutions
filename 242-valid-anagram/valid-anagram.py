class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(tuple(s))==sorted(tuple(t)):
            return True
        else:
            return False