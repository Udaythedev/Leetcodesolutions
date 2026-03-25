class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Rp = []
        for i in accounts:
            tm = 0
            for j in i:
                tm+=j
            Rp.append(tm)
        return max(Rp)
