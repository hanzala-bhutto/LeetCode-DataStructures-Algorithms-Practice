from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price

            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    h = Solution()
    print("The number is", h.maxProfit(prices))


# The time complexity of the maxProfit method in the Solution class 
# is O(n), where n is the length of the input list prices. 
# This is because the method uses a single loop to iterate over the prices list once.

# The space complexity of the maxProfit method is O(1), 
# which is constant space. This is because the method only 
# uses a constant amount of additional space to store the max_profit 
# and min_price variables. The space used by the input list is
# not counted as part of the space complexity.
