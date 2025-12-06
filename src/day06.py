import sys
from itertools import zip_longest


def read_data(filename):
    """Read and process the data from the file."""
    with open(filename) as file:
        return file.read().strip().split("\n")


def main():
    """Main function for script execution."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_data(filename)

    part1 = 0
    data1 = [x.strip().split() for x in data]
    ops = data1[-1]
    height = len(data1) - 1
    width = len(ops)
    for w in range(width):
        expression = ""
        for h in range(height - 1):
            expression += data1[h][w] + ops[w]
        expression += data1[-2][w]
        part1 += eval(expression)

    part2 = 0
    data2 = [list(x) for x in data[:-1]]
    data2 = [list(x) for x in zip_longest(*data2, fillvalue=" ")]
    data2 = ["".join(x).strip() for x in data2]
    ops = data[-1].split()

    ptr = 0
    for op in ops:
        expression = ""
        for i in range(ptr, len(data2)):
            if data2[i] == "":
                ptr = i + 1
                break
            expression += data2[i] + op
        part2 += eval(expression[:-1])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
