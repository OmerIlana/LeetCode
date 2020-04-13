class Solution(object):
    
    def maxProfit(self, prices):
        max_profit = 0

        if prices == None or len(prices) < 2:
            print("Not enought data")
            return max_profit
    
        buying_price = prices[0]
        buying_day = 1
        selling_price = 0
        selling_day = None
        
        for day, price in enumerate(prices[1:], start=2):
            if price < buying_price:
                buying_price = price
                buying_day = day
            elif max_profit < price - buying_price:
                selling_price = price
                selling_day = day
                max_profit = selling_price- buying_price

        if max_profit > 0:
            COIN='$'
            print("Buy on day",  buying_day,  "at", buying_price,  COIN)
            print("Sell on day", selling_day, "at", selling_price, COIN)
            print("Gain", max_profit, COIN)
        else:
            print("No profit here")
            
        return max_profit 