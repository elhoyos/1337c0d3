# uv run 0_1_knapsack.py

def knapsack(input):
    (_, capacity), *rest = input
    memo = {}

    # top-down
    def knapsack_recursive(i, rem):
        total_value = 0
        if i == len(rest):
            return 0

        if memo.get(i, {}).get(rem) != None:
            return memo[i][rem]

        weight = rest[i][0]
        value = rest[i][1]

        memo.setdefault(i, {})
        memo[i].setdefault(rem, value)

        if weight <= rem:
            total_value = max(
                knapsack_recursive(i + 1, rem),
                knapsack_recursive(i + 1, rem - weight) + value
            )

        memo[i][rem] = total_value

        return memo[i][rem]

    class Memo(dict):
        def __missing__(self, key):
            return 0

    # bottom-up
    def knapsack_iterative(values, weights, capacity):
        memo = Memo()
        n = len(values)
        for i in range(n - 1, -1, -1):
            for c in range(capacity + 1):
                memo[(i, c)] = memo[(i + 1, c)]
                if weights[i] <= c:
                    memo[(i, c)] = max(
                        memo[(i, c)],
                        memo[(i + 1, c - weights[i])] + values[i]
                    )

        return memo[(0, capacity)]

    values = []
    weights = []
    for w, v in rest:
        values.append(v)
        weights.append(w)

    # return knapsack_recursive(0, capacity)
    return knapsack_iterative(values, weights, capacity)

def test():
  tests = [
     [
        [
            (3, 8), # 1st entry: number of entries (N), knapsack capacity (W)
            (3, 30), # successive entries: weight, value
            (4, 50),
            (5, 60),
        ],
        90
     ],
     [
        [
            (5, 5),
            (1, 1000000000),
            (1, 1000000000),
            (1, 1000000000),
            (1, 1000000000),
            (1, 1000000000),
        ],
        5000000000
     ],
     [
        [
            (6, 15),
            (6, 5),
            (5, 6),
            (6, 4),
            (6, 6),
            (3, 5),
            (7, 2),
        ],
        17
     ]
  ]

  for input, want in tests:
        res = knapsack(input)
        if want != res:
            raise RuntimeError(f"Unexpected response, want={want}, got={res}")

if __name__ == "__main__":
    test()