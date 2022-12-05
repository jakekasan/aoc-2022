from pathlib import Path
import re

def load_test_data():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def load_data():
    return Path("./data/day5.txt").read_text()

def parse_stacks(stacks_raw):
    n_stacks = stacks_raw.splitlines()[-1].split()
    stacks = {n: [] for n in n_stacks}
    for line in stacks_raw.splitlines()[:-1]:
        for stack_n, idx in enumerate(range(1, (len(stacks) * 4) + 2, 4), start=1):
            try:
                value = line[idx]
                if not value or value == " ":
                    continue
                stacks[str(stack_n)].insert(0, line[idx])
            except:
                pass
    return stacks

def parse_moves(moves_raw):
    pat = r"move ([\d]+) from ([\d]+) to ([\d]+)"
    moves = []
    for line in moves_raw.splitlines():
        match = re.match(pat, line)
        if match is None:
            continue
        (n, source, dest) = match.groups()
        moves.append((int(n), source, dest))
    return moves
            

def parse(data: str):
    stacks, moves = data.split("\n\n")
    return stacks, moves

def part1():
    data = load_data()
    stacks, moves = parse(data)
    stacks = parse_stacks(stacks)
    moves = parse_moves(moves)
    for move in moves:
        n, source, destination = move
        for _ in range(n):
            item = stacks[source].pop()
            stacks[destination].append(item)
    
    end_crates = []
    for n in sorted(stacks, key=int):
        end_crates.append(stacks[n][-1])
    return "".join(end_crates)

def part2():
    data = load_data()
    stacks, moves = parse(data)
    stacks = parse_stacks(stacks)
    moves = parse_moves(moves)
    for move in moves:
        n, source, destination = move
        to_move = stacks[source][-n:]
        stacks[source] = stacks[source][:-n]
        stacks[destination].extend(to_move)

    end_crates = []
    for n in sorted(stacks, key=int):
        end_crates.append(stacks[n][-1])
    return "".join(end_crates)

if __name__ == "__main__":
    print(f"{part1() = }")
    print(f"{part2() = }")
