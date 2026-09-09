# ruby -r validator.rb -e 'test'

RESULTS = {
  x_wins: "X wins",
  o_wins: "O wins",
  draw: "Draw"
}

DIRS = {
  h: [0, 1],
  v: [1, 0],
  du: [-1, -1],
  dd: [1, 1]
}

def validate(grid)
  cols = grid.length
  rows = grid[0].length

  candidate = "-"

  i = 0
  win = false
  while i < rows
    j = 0
    while j < cols
      candidate = grid[i][j]

      DIRS.keys.each do |dir|
        marks = walk(grid, i, j, candidate, cols, rows, dir)
        break if win = marks.count { |r| r } == 3
      end
      
      break if win

      j += 1
    end

    break if win

    i += 1
  end

  result = if win && candidate == "X"
    RESULTS[:x_wins]
  elsif win && candidate == "O"
    RESULTS[:o_wins]
  else
    RESULTS[:draw]
  end

  result
end

# dst
def walk(grid, i, j, candidate, cols, rows, dir, marks = [])
  marks << (grid[i][j] == candidate)
  # puts "cell=#{grid[i][j]}, candidate=#{candidate}, i=#{i}, j=#{j}, dir=#{dir} marks=#{marks}"
  # edge
  if i+1 == cols || j+1 == rows
    return marks
  end

  step_i, step_j = DIRS[dir]
  new_i = i + step_i
  new_j = j + step_j
  if new_i >= 0 && new_j < rows && new_j >= 0 && new_j < cols
    walk(grid, new_i, new_j, candidate, cols, rows, dir, marks)
  end

  marks
end

def test
  tests = [
    {    
      expect: "Draw",
      grid: [
        ["O", "X", "O"],
        ["O", "X", "X"],
        ["X", "O", "X"]
      ],
    },

    {  
      expect: "Draw",
      grid: [
        ["X", "O", "O"],
        ["-", "-", "-"],
        ["-", "-", "-"]
      ],
    },

    {  
      expect: "Draw",
      grid: [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
      ],
    },

    {  
      expect: "X wins",
      grid: [
        ["X", "O", "O"],
        ["X", "-", "-"],
        ["X", "-", "-"]
      ],
    },

    {  
      expect: "O wins",
      grid: [
        ["X", "O", "O"],
        ["-", "O", "X"],
        ["X", "O", "-"]
      ],
    },

    {    
      expect: "O wins",
      grid: [
        ["O", "O", "O"],
        ["-", "X", "-"],
        ["X", "-", "X"]
      ],
    },
  ]

  tests.each do |test|
    grid = test[:grid]
    expect = test[:expect]
    res = validate(grid)
    if expect != res
      raise StandardError.new("Unexpected validation, want=#{expect}, got=#{res}")
    end
  end
end