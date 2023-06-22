# To run in leetCode
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         buy = prices[0]
#         profit=0

#         for sell in prices:
#             if buy < sell:
#                 profit=max(profit,sell-buy)
#             else:
#                 buy=sell

#         return profit

# Time Complexity : O(n)
# Space Complexity : O(1)
def maxProfit(prices: list[int]) -> int:

    buy = prices[0]
    profit=0

    for sell in prices:
        if buy < sell:
            profit=max(profit,sell-buy)
        else:
            buy=sell

    return profit

# Test Case 1
prices = [7,1,5,3,6,4]
result = maxProfit(prices)
print(result)

# Test Case 2
prices = [7,6,4,3,1]
result = maxProfit(prices)
print(result)

# Test Case 3
prices = [2,4,1]
result = maxProfit(prices)
print(result)