from collections import deque
from pathlib import Path


def load_data():
    return Path("./data/day6.txt").read_text()

def part1():
    data = load_data()

    buffer = deque()
    count = 0
    for char in data:
        count += 1
        buffer.append(char)
        if len(buffer) != 5:
            continue
        buffer.popleft()
        if len(buffer) == len(set(buffer)):
            return count

def part2():
    data = load_data()

    buffer = deque()
    count = 0
    for char in data:
        count += 1
        buffer.append(char)
        if len(buffer) != 15:
            continue
        buffer.popleft()
        if len(buffer) == len(set(buffer)):
            return count

if __name__ == "__main__":
    print(f"{part1() = }")
    print(f"{part2() = }")
