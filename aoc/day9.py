from pathlib import Path

def load_data():
    return Path("./data/day9.txt").read_text()

def part1(data=None):
    if data is None:
        data = load_data()
    head_moves = []
    for line in data.splitlines():
        dir_, count = line.split(" ")
        count = int(count)
        if dir_ == "D":
            for _ in range(count):
                head_moves.append((0, -1))
        if dir_ == "U":
            for _ in range(count):
                head_moves.append((0, 1))
        if dir_ == "L":
            for _ in range(count):
                head_moves.append((-1, 0))
        if dir_ == "R":
            for _ in range(count):
                head_moves.append((1, 0))
    tail_moves = set([(0,0)])
    head = last_head = tail = (0,0)
    for move in head_moves:
        last_head = head
        head = (head[0] + move[0], head[1] + move[1])
        diff = sum(abs(a - b)**2 for a, b in zip(head, tail))**0.5
        if diff >= 2:
            tail_moves.add(last_head)
            tail = last_head
    return len(tail_moves)

def part2(data=None):
    if data is None:
        data = load_data()
    head_moves = []
    for line in data.splitlines():
        dir_, count = line.split(" ")
        count = int(count)
        if dir_ == "D":
            for _ in range(count):
                head_moves.append((0, -1))
        if dir_ == "U":
            for _ in range(count):
                head_moves.append((0, 1))
        if dir_ == "L":
            for _ in range(count):
                head_moves.append((-1, 0))
        if dir_ == "R":
            for _ in range(count):
                head_moves.append((1, 0))
    visited = set([(0,0)])
    rope = [(0,0) for _ in range(10)]
    for move in head_moves:
        rope[-1] = (rope[-1][0] + move[0], rope[-1][1] + move[1])
        for i in range(len(rope) - 2, -1, -1):
            this = rope[i]
            prev = rope[i+1]
            (dx, dy) = (prev[0] - this[0], prev[1] - this[1])
            if 2 in map(abs, (dx, dy)):
                mx, my = ((dx // abs(dx)) if dx != 0 else 0, (dy // abs(dy)) if dy != 0 else 0)
                x, y = this
                rope[i] = (x + mx, y + my)
        visited.add(rope[0])
    return len(visited)

if __name__ == "__main__":
    test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    test2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    print(f"{part1() = }")
    print(f"{part2() = }")