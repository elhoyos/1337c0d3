# uv run num_islands_dfs.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import copy

def dfsWalk(grid, i, j, m, n, seen) -> None:
    # print(f"i={i}, j={j}, count={count}")
    if grid[i][j] == '0' or (i, j) in seen:
        return

    seen.add((i, j))

    dirs = ((0, 1), (0, -1), (-1, 0), (1, 0))
    for step_i, step_j in dirs:
        new_i = i + step_i
        new_j = j + step_j
        if new_i >=0 and new_i < m and new_j >= 0 and new_j < n:
            dfsWalk(grid, new_i, new_j, m, n, seen)
    

def numIslands(grid) -> int:
    # depth first search strategy: an island is counted by exploring its boundaries (0's)
    # - in the presence of an unseen land (1), walk adjacent cells in all directions until a boundary is found
    # - do the same recursively
    #
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    count = 0
    m = len(grid)
    n = len(grid[0])
    seen = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i, j) not in seen:
                count += 1
                dfsWalk(grid, i, j, m, n, seen)

    return count

def test():
    tests = [
        [
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ],
        [
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ],
        [
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","1","0","1","1"]
            ],
            4
        ],
        [
            [["1","0","1","1","0","1","1"]],
            3
        ],
        [
            [
                ["1","1","1"],
                ["0","1","0"],
                ["1","1","1"]
            ],
            1
        ],
        [
            [
                ["1","0","1"],
                ["1","1","1"],
                ["1","0","1"]
            ],
            1
        ],
        [
            [
                ["1","1","1","1","1"],
                ["1","1","0","0","1"],
                ["0","0","1","0","1"],
                ["1","1","1","1","1"]
            ],
            1
        ],
        [
            [
                ["1","1","1","1","1","0","1","1","1","1"],
                ["1","0","1","0","1","1","1","1","1","1"],
                ["0","1","1","1","0","1","1","1","1","1"],
                ["1","1","0","1","1","0","0","0","0","1"],
                ["1","0","1","0","1","0","0","1","0","1"],
                ["1","0","0","1","1","1","0","1","0","0"],
                ["0","0","1","0","0","1","1","1","1","0"],
                ["1","0","1","1","1","0","0","1","1","1"],
                ["1","1","1","1","1","1","1","1","0","1"],
                ["1","0","1","1","1","1","1","1","1","0"]
            ],
            2
        ],
        [
            [
                ["1","1","1","1","1","0","1","1","1","1"],
                ["0","1","1","0","1","1","1","0","1","1"],
                ["1","0","1","0","1","1","0","1","0","1"],
                ["1","0","1","1","0","1","1","1","1","1"],
                ["1","1","0","0","1","1","1","1","1","1"],
                ["1","1","0","1","1","1","1","1","1","1"],
                ["1","1","1","1","1","1","1","1","0","1"],
                ["0","1","1","0","1","1","1","1","1","0"],
                ["1","1","0","1","1","0","1","1","1","1"],
                ["0","1","1","1","1","1","0","1","1","1"]
            ],
            1
        ]
    ]

    for input, want in tests:
        res = numIslands(input)
        if want != res:
            raise RuntimeError(f"Unexpected response, want={want}, got={res}")

if __name__ == "__main__":
    test()
