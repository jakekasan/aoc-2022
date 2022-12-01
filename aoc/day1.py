from pathlib import Path

def part1():
    data = Path("./data/day1.txt").read_text()
    max_total = 0
    this_total = 0
    for line in data.splitlines():
        if line == "":
            max_total = max([max_total, this_total])
            this_total = 0
            continue
        this_total += int(line)

    return max_total

def part2():
    data = Path("./data/day1.txt").read_text()
    totals = []
    this_total = 0
    for line in data.splitlines():
        if line == "":
            totals.append(this_total)
            this_total = 0
            continue
        this_total += int(line)

    top_3 = sorted(totals, reverse=True)[:3]
    return sum(top_3)

if __name__ == "__main__":
    print("part1", part1())
    print("part2", part2())