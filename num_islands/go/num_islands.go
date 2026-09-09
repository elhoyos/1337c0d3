package num_islands

func numIslands(grid [][]byte) int {
	count := 0
	m := len(grid)
	n := len(grid[0])
	seen := make([][]bool, m)
	for i := range seen {
		seen[i] = make([]bool, n)
	}

	for i := range m {
		for j := range n {
			if grid[i][j] == '1' && !seen[i][j] {
				count += 1
				gatherIsland(grid, seen, i, j, m, n)
			}
		}
	}
		
	return count
}

// DST
func gatherIsland(grid [][]byte, seen [][]bool, i int, j int, m int, n int) {
	if grid[i][j] == '0' || seen[i][j] {
		return
	}

	seen[i][j] = true

	dirs := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for dir_ix := range dirs {
		dir := dirs[dir_ix]
		next_i := i + dir[0]
		next_j := j + dir[1]

		if next_i >= 0 && next_i < m && next_j >=0 && next_j < n {
			gatherIsland(grid, seen, next_i, next_j, m, n)
		}
	}
}
