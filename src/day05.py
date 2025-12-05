import sys


def read_data(filename):
    """Read and process the data from the file."""
    with open(filename) as file:
        return file.read().strip().split("\n\n")


def main():
    """Main function for script execution."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_data(filename)

    range_list = data[0].split("\n")
    available_list = map(int, data[1].split("\n"))

    ranges = []
    for x in range_list:
        a, b = map(int, x.split("-"))
        ranges.append((a, b))

    part1 = 0
    for x in available_list:
        for a, b in ranges:
            if a <= x <= b:
                part1 += 1
                break

    ranges = sorted(ranges)
    merged = [ranges[0]]

    for a, b in ranges[1:]:
        if a <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))

    part2 = sum(b - a + 1 for a, b in merged)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
