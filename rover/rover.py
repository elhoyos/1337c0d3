# uv run rover.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

from enum import Enum

class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Rover x={self.x}, y={self.y}>"

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

def test():
    class Move(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4

    tests = [
        [
            (1, 1),
            [Move.LEFT, Move.RIGHT, Move.UP, Move.DOWN],
            (1, 1),
        ],
        [
            (0, 0),
            [Move.DOWN, Move.RIGHT, Move.UP, Move.UP, Move.UP, Move.LEFT],
            (0, 2),
        ]
    ]

    for test in tests:
        init, moves, exp = test
        r = Rover(*init)

        for move in moves:
            match move:
                case Move.LEFT:
                    r.left()
                case Move.RIGHT:
                    r.right()
                case Move.UP:
                    r.up()
                case Move.DOWN:
                    r.down()
                case _:
                    raise Exception(f"Unsupported test move {move}")

        position = (r.x, r.y)
        if exp != position:
            raise Exception(f"Unexpected position, want={exp} got={position}")

def help():
    return """
    A Rover moved by your keyboard. Use:
    - a: Left
    - d: Right
    - w: Up
    - s: Down

    "h" to print this help.
    "test" to run the unit tests.
    "q" to quit.
    """.strip()

PROMPT = "> "

def main() -> None:
    print("Welcome to Rover!")
    print(help())

    rover = Rover(0, 0)

    while True:
        print(PROMPT, end="")
        line = input()

        match line:
            case "a":
                rover.left()
            case "d":
                rover.right()
            case "w":
                rover.up()
            case "s":
                rover.down()
            case "test":
                print("Running unit tests...")
                test()
                print("✅ All tests passed")
                exit(0)
            case "q":
                exit(0)
            case _:
                print(help())

        print(rover)


if __name__ == "__main__":
    main()
