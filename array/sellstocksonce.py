class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        maxi=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])
            maxi=max(maxi,prices[i]-mini)
        return maxi