// node convert_time.ts

function convertTime(current: string, correct: string): number {
  // intituition: since all minutes to operate are multiples of 60, we can
  // loop through each in descending order until we reach the time

  if (current == correct) return 0

  let nOps = 0;
  const [cHours, cMinutes] = current.split(':').map((x) => parseInt(x));
  const [rHours, rMinutes] = correct.split(':').map((x) => parseInt(x));
  let diffMinutes = (rHours * 60 + rMinutes) - (cHours * 60 + cMinutes);

  const minuteOps = [60, 15, 5, 1]
  for (const minutes of minuteOps) {
      const res = Math.trunc(diffMinutes / minutes);
      diffMinutes -= minutes * res;
      nOps += res;
  }

  return nOps;
}

type Input = Parameters<typeof convertTime>;
type Test = [Input, number];

function test() {
  const tests: Test[] = [
    [
        [
            "02:30",
            "04:35"
        ],
        3
    ],
    [
        [
            "11:00",
            "11:01"
        ],
        1
    ],
  ];

  for (const [input, exp] of tests) {
    const res = convertTime(...input);
    if (exp != res) {
      throw new Error(`Unexpected result, want=${exp}, got=${res}`);
    }
  }
}

test()