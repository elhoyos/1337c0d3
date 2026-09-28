# uv run 0_1_knapsack.py

def knapsack(input):
    first, *rest = input
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

    # bottom-up
    def knapsack_iterative(values, weights, capacity):
        n = len(values)
        for i in range(n + 1):
            for rem in range(capacity + 1):
                if i == 0 or rem == 0:
                    memo[(i, rem)] = 0
                    continue

                pick = 0

                if weights[i - 1] <= rem:
                    pick = memo[(i - 1, rem - weights[i - 1])] + values[i - 1]

                no_pick = memo[(i - 1, rem)]

                memo[(i, rem)] = max(pick, no_pick)

        return memo[(n, capacity)]

    values = []
    weights = []
    for w, v in rest:
        values.append(v)
        weights.append(w)

    # return knapsack_recursive(0, first[1])
    return knapsack_iterative(values, weights, first[1])

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