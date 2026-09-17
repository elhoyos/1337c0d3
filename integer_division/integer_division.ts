// node integer_division.ts

const MIN_QUOTIENT = -Math.pow(2, 31);
const MAX_QUOTIENT = Math.pow(2, 31) - 1;

function withinRange(quotient: number) {
    if (quotient < MIN_QUOTIENT) return MIN_QUOTIENT;
    if (quotient > MAX_QUOTIENT) return MAX_QUOTIENT;
    return quotient;
}

function positive(i: number) {
    return i >= 0 ? i : ~i + 1;
}

function divide(dividend: number, divisor: number): number {
    const isNegativeQuotient = dividend < 0 !== divisor < 0;
    
    if (dividend == divisor) return 1;

    let pDividend = positive(dividend);
    const pDivisor = positive(divisor);
    let quotient = 0;
    while (pDivisor <= pDividend) {
        let jump = pDivisor;
        let multiple = 1;

        while (jump + jump <= pDividend) {
            jump += jump;
            multiple += multiple;
        }

        pDividend -= jump;
        quotient += multiple;
            
        console.log(`dividend=${pDividend}, divisor=${pDivisor}, quotient=${quotient}, jump=${jump}`)
    }

    if (isNegativeQuotient) {
        quotient = -quotient;
    }

    return withinRange(quotient);
};

type Input = Parameters<typeof convertTime>;
type Test = [Input, number];

function test() {
  const tests: Test[] = [
    [
        [10, 3],
        3,
    ],
    [
        [7, -3],
        -2,
    ],
    [
        [2147483647, -1],
        -2147483647
    ],
  ];

  for (const [input, exp] of tests) {
    const res = divide(...input);
    if (exp != res) {
      throw new Error(`Unexpected result, want=${exp}, got=${res}`);
    }
  }
}

test()