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
            s = str(x)
            length = len(s)

            if length % 2 == 0:
                width = length // 2
                if s[:width] == s[width:]:
                    part1 += x

            for w in range(1, length // 2 + 1):
                if length % w == 0:
                    chunk = s[:w]
                    if all(s[i : i + w] == chunk for i in range(w, length, w)):
                        part2 += x
                        break

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
