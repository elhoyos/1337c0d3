// node coin_change.ts

type Memo = { [key: string]: number };

function coinChange(coins: number[], amount: number): number {
  const memo: Memo = {};

  function solve(remaining: number): number {
    if (remaining == 0) return 0;
    if (remaining < 0) return -1;
    if (memo[remaining]) return memo[remaining];

    let min_count = Infinity;

    for (const coin of coins) {
      const res = solve(remaining - coin);
      if (res != -1) {
        min_count = Math.min(min_count, 1 + res);
      }
    }

    memo[remaining] = min_count == Infinity ? -1 : min_count;
    return memo[remaining];
  }

  return solve(amount)
}

type Input = Parameters<typeof coinChange>;
type Test = [Input, number];

function test() {
  const tests: Test[] = [
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
  ];

  for (const [input, exp] of tests) {
    const res = coinChange(...input);
    if (exp != res) {
      throw new Error(`Unexpected result, want=${exp}, got=${res}`);
    }
  }
}

test()