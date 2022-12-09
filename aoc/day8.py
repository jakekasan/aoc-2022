from functools import reduce
import operator
from pathlib import Path


def load_data():
    return Path("./data/day8.txt").read_text()

def part1(data = None):
    if data is None:
        data = load_data()
    grid = []
    for line in data.splitlines():
        grid.append(list(map(int, line)))
    visible = {(x, y) for y in (0, len(grid) - 1) for x in range(len(grid[0]))}
    for y, line in enumerate(grid):
        max_ = grid[y][0]
        visible.add((0, y))
        visible.add((len(line) - 1, y))
        for x in range(1, len(line) - 1):
            if line[x] > line[x-1] and line[x] > max_:
                visible.add((x, y))
            max_ = max([line[x], max_])
        max_ = grid[y][len(line)-1]
        for x in range(len(line) - 2, 0, -1):
            if line[x] > line[x+1] and line[x] > max_:
                visible.add((x, y))
            max_ = max([line[x], max_])
    for x in range(1, len(grid[0])):
        max_ = grid[0][x]
        for y in range(1, len(grid)):
            if grid[y][x] > grid[y-1][x] and grid[y][x] > max_:
                visible.add((x, y))
            max_ = max([grid[y][x], max_])
        max_ = grid[len(grid) - 1][x]
        for y in range(len(grid) - 2, 0, -1):
            if grid[y][x] > grid[y+1][x] and grid[y][x] > max_:
                visible.add((x, y))
            max_ = max([grid[y][x], max_])
    return len(visible)

def part2(data=None):
    trees = {}
    if data is None:
        data = load_data()
    for y, line in enumerate(data.splitlines()):
        for x, tree in enumerate(list(map(int, line))):
            trees[(x, y)] = tree

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    best = 0
    for (x, y), tree in trees.items():
        counts = []
        for direction in directions:
            x2, y2 = x, y
            count = 0
            while True:
                dx, dy = direction
                x2, y2 = x2 + dx, y2 + dy
                other_tree = trees.get((x2, y2))
                if other_tree is None:
                    break
                count += 1
                if other_tree >= tree:
                    break
            counts.append(count)
        if counts:
            best = max(best, reduce(operator.mul, counts, 1))
    return best

if __name__ == "__main__":
    test = """30373
25512
65332
33549
35390"""
    print(f"{part1() = }")
    print(f"{part2() = }")
