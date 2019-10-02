"""
Problem statement: Given a target amount V cents and a list of denominations of
n coins, i.e. we have coinValue[i] (in cents) for coin types i from [0...n - 1],
what is the minimum number of coins that we must use to represent amount V?
Assume that we have an unlimited supply of coins of any type.
"""

class Solution:
    """
    Greedy approach: continuously subtract the value of the largest coin.
    """
    coins = [25, 10, 5, 1]

    def change(self, v: int) -> int:
        counter = 0

        for c in self.coins:
            while c <= v:
                v -= c
                counter += 1

        return counter


def main():
    sol = Solution()
    print(sol.change(41))
    print(sol.change(0))
    print(sol.change(99))


if __name__ == '__main__':
    main()
