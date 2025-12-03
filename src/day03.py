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
    for line in data:
        line = list(map(int, line))
        idx_a, a = max(enumerate(line[:-1]), key=lambda x: x[1])
        b = max(line[idx_a + 1 :])
        part1 += int(str(a) + str(b))

    part2 = 0
    for line in data:
        line = list(map(int, line))

        width = 11  # Needed width - 1

        solution = ""
        idx, val = max(enumerate(line[:-width]), key=lambda x: x[1])
        solution += str(val)
        width -= 1

        while width >= 0:
            if width > 0:
                tmp_idx, val = max(
                    enumerate(line[idx + 1 : -width]), key=lambda x: x[1]
                )
                idx += tmp_idx + 1
            else:
                val = max(line[idx + 1 :])

            solution += str(val)
            width -= 1

        part2 += int(solution)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
