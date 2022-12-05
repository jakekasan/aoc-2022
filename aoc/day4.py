from pathlib import Path

def part1():
    data = Path("./data/day4.txt").read_text()

    count = 0
    for row in data.splitlines():
        left, right = row.split(",")
        lmin, lmax = map(int, left.split("-"))
        rmin, rmax = map(int, right.split("-"))
        if lmax <= rmax and lmin >= rmin:
            count += 1
        elif rmax <= lmax and rmin >= lmin:
            count += 1
    return count

def part2():
    data = Path("./data/day4.txt").read_text()

    count = 0
    for row in data.splitlines():
        left, right = row.split(",")
        lmin, lmax = map(int, left.split("-"))
        rmin, rmax = map(int, right.split("-"))
        if rmin <= lmin <= rmax:
            count += 1
            continue
        if rmin <= lmax <= rmax:
            count += 1
            continue
        if lmin <= rmin <= lmax:
            count += 1
            continue
        if lmin <= rmax <= lmax:
            count += 1
            continue
    return count

if __name__ == "__main__":
    print(f"{part1() = }")
    print(f"{part2() = }")