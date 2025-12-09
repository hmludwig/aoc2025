import sys
from itertools import combinations


def read_data(filename):
    """Read and process the data from the file."""
    with open(filename) as file:
        data = file.read().strip().split("\n")
        return sorted([tuple(map(int, x.split(","))) for x in data])


def euclidean(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2))


def main():
    """Main function for script execution."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_data(filename)

    part1 = 0

    closest = sorted(
        combinations(data, 2), key=lambda pair: euclidean(*pair), reverse=True
    )

    sets = []
    for _ in range(1000):
        pair = closest.pop()

        # Find all sets containing either point
        matching = [s for s in sets if pair[0] in s or pair[1] in s]

        if not matching:
            sets.append({pair[0], pair[1]})
        elif len(matching) == 1:
            matching[0].add(pair[0])
            matching[0].add(pair[1])
        else:
            # Merge two sets
            matching[0].update(matching[1])
            sets.remove(matching[1])

    sets = sorted(sets, key=len, reverse=True)
    part1 = len(sets[0]) * len(sets[1]) * len(sets[2])

    part2 = 0

    closest = sorted(
        combinations(data, 2), key=lambda pair: euclidean(*pair), reverse=True
    )

    needed_size = len(data)
    current_size = 0
    sets = []
    while current_size != needed_size:
        pair = closest.pop()

        # Find all sets containing either point
        matching = [s for s in sets if pair[0] in s or pair[1] in s]

        if not matching:
            sets.append({pair[0], pair[1]})
        elif len(matching) == 1:
            matching[0].add(pair[0])
            matching[0].add(pair[1])
        else:
            # Merge two sets
            matching[0].update(matching[1])
            sets.remove(matching[1])

        sets = sorted(sets, key=len, reverse=True)
        current_size = len(sets[0])

    part2 = pair[0][0] * pair[1][0]

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
