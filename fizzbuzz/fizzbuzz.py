# uv run fizzbuzz.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///


def fizzbuzz(n):
    out = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))

    return out

def test():
    tests = [
        [3, ["1","2","Fizz"]],
        [5, ["1","2","Fizz","4","Buzz"]],
        [15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]],
    ]

    for n, exp in tests:
        res = fizzbuzz(n)
        if exp != res:
            raise RuntimeError(f"Unexpected result for n={n}, want={exp}, got={res}")


if __name__ == "__main__":
    test()
