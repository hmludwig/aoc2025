import sys


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
    pos = 50
    for line in data:
        direction, amount = line[0], int(line[1:])
        if direction == "L":
            pos = (pos - amount) % 100
            if pos == 0:
                part1 += 1
        else:
            pos = (pos + amount) % 100
            if pos == 0:
                part1 += 1

    part2 = 0
    pos = 50
    for line in data:
        direction, amount = line[0], int(line[1:])
        part2 += amount // 100
        remainder = amount % 100

        if direction == "L":
            if 0 < pos <= remainder:
                part2 += 1
            pos = (pos - remainder) % 100
        else:
            if pos + remainder >= 100:
                part2 += 1
            pos = (pos + remainder) % 100

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
