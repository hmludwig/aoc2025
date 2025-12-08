import sys
from copy import deepcopy
from functools import lru_cache


def read_data(filename):
    """Read and process the grid from the file."""
    with open(filename) as file:
        return [list(x) for x in file.read().strip().split("\n")]


def print_grid(grid):
    for row in grid:
        print("".join(str(cell) for cell in row))
    print()


def main():
    """Main function for script execution."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_data(filename)

    grid = deepcopy(data)
    width = len(grid[0])
    beams = {grid[0].index("S")}
    part1 = 0

    for i, row in enumerate(grid[1:], start=1):
        next_beams = set()
        for beam in beams:
            if grid[i][beam] == "^":
                part1 += 1
                for new_beam in (beam - 1, beam + 1):
                    if 0 <= new_beam < width:
                        next_beams.add(new_beam)
                        grid[i][new_beam] = "|"
            else:
                grid[i][beam] = "|"
                next_beams.add(beam)
        beams = next_beams

    print_grid(grid)

    @lru_cache(maxsize=None)
    def count_paths(i, beam):
        if i == height:
            return 1
        if data[i][beam] == "^":
            total = 0
            for new_beam in (beam - 1, beam + 1):
                if 0 <= new_beam < width:
                    total += count_paths(i + 1, new_beam)
            return total
        else:
            return count_paths(i + 1, beam)

    height = len(data)
    beam = data[0].index("S")
    part2 = count_paths(1, beam)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
