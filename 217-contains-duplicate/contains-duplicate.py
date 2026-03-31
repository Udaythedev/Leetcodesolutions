class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numl=set()
        for i in nums:
            if i not in numl:
                numl.add(i)
            else:
                return True
        return False