# uv run coin_change.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///


def coinChange(coins, amount):
    memo = {}
    inf = float('inf')

    def solve(remaining):
        if remaining == 0: return 0
        if remaining < 0: return -1
        if remaining in memo: return memo[remaining]

        min_coins = inf

        for coin in coins:
            res = solve(remaining - coin)
            if res != -1:
                min_coins = min(min_coins, 1 + res)

        memo[remaining] = min_coins if min_coins != inf else -1
        return memo[remaining]

    return solve(amount)

def test():
    tests = [
        [
            [
                [1,2,5],
                11
            ],
            3
        ],
        [
            [
                [2],
                3
            ],
            -1
        ],
        [
            [
                [1],
                0
            ],
            0
        ],
        [
            [
                [186,419,83,408],
                6249
            ],
            20
        ],
    ]

    for input, want in tests:
        res = coinChange(*input)
        if want != res:
            raise RuntimeError(f"Unexpected response, want={want}, got={res}")

if __name__ == "__main__":
    test()
