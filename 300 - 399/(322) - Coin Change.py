class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        result = 0
        coins.sort(reverse=True)
        for coin in coins:
            result += amount // coin
            amount %= coin

        if amount:
            return -1
        return result


print(Solution.coinChange(Solution, [186,419,83,408], 6249))