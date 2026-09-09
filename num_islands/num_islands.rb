# ruby -r ./num_islands.rb -e 'test'

# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
  rows = grid.length
  cols = grid[0].length
  count = 0
  seen = grid.map { |c| c.map { false } }

  i = 0
  while i < rows
    j = 0
    while j < cols
      count += 1 if grid[i][j] == '1' && !seen[i][j]
      dst_walk(grid, i, j, seen, cols, rows)
      j += 1
    end
    i += 1
  end

  count
end

def dst_walk(grid, i, j, seen, cols, rows)
  # break when finds an edge of the island or if already walked
  if grid[i][j] == '0' || seen[i][j]
    return
  end

  # mark it as seen when part of the island
  seen[i][j] = true
    
  dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  dirs.each do |(step_i, step_j)|
    new_i = i + step_i
    new_j = j + step_j

    if new_i >= 0 && new_i < rows && new_j >= 0 && new_j < cols
      dst_walk(grid, new_i, new_j, seen, cols, rows)
    end
  end
end

def test
  tests = [
    {
      grid: [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
      ],
      expected: 1
    },
    {
      grid: [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
      ],
      expected: 3
    }
  ]

  tests.each do |t|
    grid = t[:grid]
    expected = t[:expected]
    result = num_islands(grid)
    if expected != result
      raise StandardError.new("Unexpected number of islands, want=#{expected}, got=#{result}")
    end
  end
end