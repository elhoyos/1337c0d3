# uv run integers_division.py

# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

def divide(dividend, divisor):
    MAX_QUOTIENT = 2 ** 31 - 1
    MIN_QUOTIENT = -2 ** 31

    if dividend == 0: return 0
    if dividend == divisor: return 1

    is_negative = False
    if not (dividend > 0 and divisor > 0):
        is_negative = True

    quotient = 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    while divisor <= dividend:
        jump = divisor
        multiple = 1

        while jump + jump <= dividend:
            jump += jump
            multiple += multiple

        dividend -= jump
        quotient += multiple

        # print(f"dividend={dividend}, divisor={divisor}, quotient={quotient}, jump={jump}")

    if is_negative:
        quotient = -quotient

    if quotient > MAX_QUOTIENT:
        return MAX_QUOTIENT

    if quotient < MIN_QUOTIENT:
        return MIN_QUOTIENT

    return quotient

def test():
    tests = [
        [
            (10, 3),
            3
        ],
        [
            (7, -3),
            -2
        ],
        [
            (10, 1),
            10
        ],
        [
            (2147483647, -1),
            -2147483647
        ],
    ]

    for input, want in tests:
        res = divide(*input)
        if want != res:
            raise RuntimeError(f"Unexpected response, want={want}, got={res}")


if __name__ == "__main__":
    test()
