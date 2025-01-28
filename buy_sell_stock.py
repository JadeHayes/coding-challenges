import unittest
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def buy_stock(prices):

    # # solution is O(n^2), exceeds timelimit
    i = 0
    j = 1

    highest_profit = 0
    while i < len(prices) - 1:
        profit = prices[j] - prices[i]
        if profit > highest_profit:
                highest_profit = profit
        j += 1
        if j >= len(prices):
            i += 1
            j = i + 1

    return highest_profit


class TestStock(unittest.TestCase):

    def test_buy_sell_stock(self):
        self.assertEqual(buy_stock([7,1,5,3,6,4]), 5)
        self.assertEqual(buy_stock([7,6,4,3,1]), 0)
        self.assertEqual(buy_stock([1, 2]), 1)
        self.assertEqual(buy_stock([2, 4, 1]), 2)
        self.assertEqual(buy_stock([1]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)