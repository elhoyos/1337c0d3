# uv run num_islands_iterative.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import copy

def numIslands(grid) -> int:
    # merge islands strategy:
    # - move left->right and up->bottom
    # - skip 0's
    # - if no cell left or up is 1, increment count
    # - if both cells left & up are 1 and belong to a different island, decrement count (merge islands)
    # - else, move to next cell
    count = 0
    m = len(grid)
    n = len(grid[0])
    islands_refs = copy.deepcopy(grid)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '0':
                continue

            if i == 0 and j == 0:
                count = 1
                islands_refs[i][j] = [[i, j]]
                continue

            refs = []
            if j-1 >= 0 and grid[i][j-1] == '1':
                refs.extend(islands_refs[i][j-1])

            if i-1 >= 0 and grid[i-1][j] == '1':
                refs.extend(islands_refs[i-1][j])

            if len(refs) == 0:
                parent = [i, j]
                print(f"island={parent}, id={id(parent)}")
                refs.append(parent)
                count += 1
            elif len(refs) == 2:
                if refs[0] != refs[1]: count -= 1

                # merge islands by converting all the refs
                island = refs.pop()
                print(f"converted={island}({id(island)}) to={refs[0]}({id(refs[0])})")
                island[0] = refs[0][0]
                island[1] = refs[0][1]

            islands_refs[i][j] = refs
            
            print(f"i={i}, j={j}, count={count}, refs={islands_refs[8]}")

    return count

def test():
    tests = [
        # [
        #     [
        #         ["1","1","1","1","0"],
        #         ["1","1","0","1","0"],
        #         ["1","1","0","0","0"],
        #         ["0","0","0","0","0"]
        #     ],
        #     1
        # ],
        # [
        #     [
        #         ["1","1","0","0","0"],
        #         ["1","1","0","0","0"],
        #         ["0","0","1","0","0"],
        #         ["0","0","0","1","1"]
        #     ],
        #     3
        # ],
        # [
        #     [
        #         ["1","1","0","0","0"],
        #         ["1","1","0","0","0"],
        #         ["0","0","1","0","0"],
        #         ["0","1","0","1","1"]
        #     ],
        #     4
        # ],
        # [
        #     [["1","0","1","1","0","1","1"]],
        #     3
        # ],
        # [
        #     [
        #         ["1","1","1"],
        #         ["0","1","0"],
        #         ["1","1","1"]
        #     ],
        #     1
        # ],
        # [
        #     [
        #         ["1","0","1"],
        #         ["1","1","1"],
        #         ["1","0","1"]
        #     ],
        #     1
        # ],
        # [
        #     [
        #         ["1","1","1","1","1"],
        #         ["1","1","0","0","1"],
        #         ["0","0","1","0","1"],
        #         ["1","1","1","1","1"]
        #     ],
        #     1
        # ],
        # [
        #     [
        #         ["1","1","1","1","1","0","1","1","1","1"],
        #         ["1","0","1","0","1","1","1","1","1","1"],
        #         ["0","1","1","1","0","1","1","1","1","1"],
        #         ["1","1","0","1","1","0","0","0","0","1"],
        #         ["1","0","1","0","1","0","0","1","0","1"],
        #         ["1","0","0","1","1","1","0","1","0","0"],
        #         ["0","0","1","0","0","1","1","1","1","0"],
        #         ["1","0","1","1","1","0","0","1","1","1"],
        #         ["1","1","1","1","1","1","1","1","0","1"],
        #         ["1","0","1","1","1","1","1","1","1","0"]
        #     ],
        #     2
        # ],
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
