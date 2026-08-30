class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0


        for _ in range(k+1):
            new_prices = prices.copy()

            for from_i, to_i, price in flights:
                if prices[from_i] == float("inf"):
                    continue
                
                new_prices[to_i] = min(prices[from_i] + price, new_prices[to_i])
            
            prices = new_prices
        
        return -1 if prices[dst] == float("inf") else prices[dst]


        
        