from pathlib import Path

def part1(data=None):
    if data is None:
        data = Path("./data/day2.txt").read_text()
    hand_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    game_scores = {
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("A", "Y"): 6,
        ("A", "X"): 3,
        ("B", "Y"): 3,
        ("C", "Z"): 3
    }
    total_score = 0

    for elf, me in (line.split(" ") for line in data.splitlines()):
        score = game_scores.get((elf, me), 0) + hand_scores.get(me, 0)
        total_score += score
    return total_score

def part2(data=None):
    if data is None:
        data = Path("./data/day2.txt").read_text()
    # hand_scores = {
    #     "X": 1,
    #     "Y": 2,
    #     "Z": 3
    # }
    game_scores = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    hand_scores = {
        ("A", "X"): 3,
        ("A", "Y"): 1,
        ("A", "Z"): 2,
        ("B", "X"): 1,
        ("B", "Y"): 2,
        ("B", "Z"): 3,
        ("C", "X"): 2,
        ("C", "Y"): 3,
        ("C", "Z"): 1,
    }
    total_score = 0

    for elf, me in (line.split(" ") for line in data.splitlines()):
        score = hand_scores.get((elf, me), 0) + game_scores.get(me, 0)
        total_score += score
    return total_score


if __name__ == "__main__":
    data="A Y\nB X\nC Z"
    print(part1())
    print(part2())
