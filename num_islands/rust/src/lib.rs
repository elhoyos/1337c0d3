// Effectively a DFS algorithm
fn gather_island(grid: &Vec<Vec<char>>, seen: &mut Vec<Vec<bool>>, i: usize, j: usize, m: usize, n: usize) {
    if grid[i][j] == '1' && !seen[i][j] {
        seen[i][j] = true;

        let i = i as isize;
        let j = j as isize;
        let dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]];

        for dir in dirs {
            let next_i = i + dir[0];
            let next_j = j + dir[1];
            if next_i >= 0 && next_i < m as isize && next_j >= 0 && next_j < n as isize {
                let new_i = next_i as usize;
                let new_j = next_j as usize;
                gather_island(grid, seen, new_i, new_j, m, n);
            }
        }
    }
}

pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
    let m = grid.len();
    let n = grid[0].len();
    let mut count = 0;
    let mut seen = vec![vec![false; n]; m];

    for i in 0..m {
        for j in 0..n {
            let cell = grid[i][j];
            if cell == '1' && !seen[i][j] {
                count += 1;
                gather_island(&grid, &mut seen, i, j, m, n);
            }
        }
    }
    
    count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_island() {
        let grid = vec![
            vec!['1','1','1','1','0'],
            vec!['1','1','0','1','0'],
            vec!['1','1','0','0','0'],
            vec!['0','0','0','0','0']
        ];
        let result = num_islands(grid);
        assert_eq!(1, result);
    }

    #[test]
    fn three_island() {
        let grid = vec![
            vec!['1','1','0','0','0'],
            vec!['1','1','0','0','0'],
            vec!['0','0','1','0','0'],
            vec!['0','0','0','1','1']
        ];
        let result = num_islands(grid);
        assert_eq!(3, result);
    }
}
