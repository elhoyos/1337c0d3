# uv run coin_change.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///


def coin_change_recursive(coins, amount):
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

def coin_change_iterative(coins, amount):
    inf = float('inf')
    memo = {0: 0}
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                memo[a] = min(
                    memo.get(a - coin, inf) + 1,
                    memo.get(a, inf)
                )

    return memo[amount] if memo.get(amount, inf) != inf else -1

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
        responses = [
            ("recursive", coin_change_recursive(*input)),
            ("iterative", coin_change_iterative(*input))
        ]
        for name, res in responses:
            if want != res:
                raise RuntimeError(f"Unexpected response for '{name}', want={want}, got={res}")

if __name__ == "__main__":
    test()
