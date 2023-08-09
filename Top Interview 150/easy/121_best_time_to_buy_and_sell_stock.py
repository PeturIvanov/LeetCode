class Solution(object):
    def maxProfit(self, prices):
        profit = 0

        buy, sell = 0, 1

        while buy < len(prices) and sell < len(prices):
            current_buy_price, current_sell_price = prices[buy], prices[sell]
            if current_buy_price > current_sell_price:
                buy = sell
                sell = buy + 1
                continue

            elif current_buy_price < current_sell_price:
                if current_sell_price - current_buy_price > profit:
                    profit = current_sell_price - current_buy_price
            sell += 1

        return profit


solution = Solution()
print(solution.maxProfit([3, 2, 6, 5, 0, 3]))

