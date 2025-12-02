import sys


def read_data(filename):
    """Read and process the data from the file."""
    with open(filename) as file:
        return file.read().strip().split(",")


def main():
    """Main function for script execution."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_data(filename)

    part1 = 0
    part2 = 0
    for element in data:
        a, b = map(int, element.split("-"))
        for x in range(a, b + 1):
            if len(str(x)) % 2 == 0:
                width = len(str(x)) // 2
                if str(x)[:width] == str(x)[width:]:
                    part1 += x

            width = len(str(x)) // 2
            for w in range(1, width + 1):
                if len(str(x)) % w == 0:
                    chunks = [str(x)[i : i + w] for i in range(0, len(str(x)), w)]
                    if len(set(chunks)) == 1:
                        part2 += x
                        break

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
