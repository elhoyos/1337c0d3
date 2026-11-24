# ruby -r ./coin_change.rb -e test

# Given an amount, return a list of coins that make up for that amount as change.
# Asume a canonical coin system: https://en.wikipedia.org/wiki/Change-making_problem#Greedy_method

CHANGE_BOX = [1, 2, 5, 10, 20, 50, 100, 200].reverse

def coin_change(amount)
  change = []

  return change if amount <= 0

  pence = amount * 100

  return change if pence - pence.to_i > 0

  CHANGE_BOX.each do |coin|
    while pence >= coin
      pence -= coin
      change << coin
    end
  end

  change
end

def test
  tests = [
    [
      0,
      []
    ],
    [
      -1,
      []
    ],
    [
      0.011,
      []
    ],
    [
      0.01,
      [1]
    ],
    [
      0.11,
      [10, 1]
    ],
    [
      0.03,
      [2, 1]
    ],
    [
      2.12,
      [200, 10, 2]
    ],
    [
      1.44,
      [100, 20, 20, 2, 2]
    ]
  ]

  tests.each do |amount, change|
    result = coin_change(amount)
    if change != result
      raise "Unexpected coin change result. want=#{change}, got=#{result}"
    end
  end
end