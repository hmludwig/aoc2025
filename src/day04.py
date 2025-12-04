import sys
import copy


def read_data(filename):
    """Read and process the data from the file."""
    with open(filename) as file:
        data = file.read().strip().split("\n")
        data = [list(x) for x in data]
        return data


def count_neighbours(grid, row, col, target):
    """Counts the occurrences of target in the neighbouring cells"""
    rows, cols = len(grid), len(grid[0])
    return sum(
        grid[row + dr][col + dc] == target
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and 0 <= row + dr < rows and 0 <= col + dc < cols
    )


def main():
    """Main function for script execution."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    grid = read_data(filename)
    rows, cols = len(grid), len(grid[0])

    part1 = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                count = count_neighbours(grid, r, c, "@")
                if count < 4:
                    part1 += 1

    part2 = 0
    while True:
        tmp_part2 = 0
        tmp_grid = copy.deepcopy(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    count = count_neighbours(grid, r, c, "@")
                    if count < 4:
                        tmp_part2 += 1
                        tmp_grid[r][c] = "."
        grid = tmp_grid

        if tmp_part2 == 0:
            break

        part2 += tmp_part2

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
