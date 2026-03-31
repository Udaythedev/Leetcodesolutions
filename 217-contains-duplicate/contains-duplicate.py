class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numl=set()
        f=0
        for i in nums:
            if i not in numl:
                numl.add(i)
            else:
                return True
        return False