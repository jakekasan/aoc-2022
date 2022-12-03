from collections import Counter
from itertools import islice
from pathlib import Path
from string import ascii_lowercase, ascii_uppercase
from textwrap import dedent


scores = {
    char: score
    for score, char in enumerate(ascii_lowercase + ascii_uppercase, start=1)
}

def part1(rucksacks=None):
    if rucksacks is None:
        rucksacks = Path("./data/day3.txt").read_text().splitlines()
    priority_sum = 0
    for i, rucksack in enumerate(rucksacks):
        first, second = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        duplicate = set()
        for item in first:
            if item in second:
                duplicate.add(item)
        priority_sum += sum(scores.get(dup) for dup in duplicate)
    return priority_sum

def part2(rucksacks=None):
    if rucksacks is None:
        rucksacks = Path("./data/day3.txt").read_text().splitlines()
    
    priority_sum = 0
    
    it = iter(rucksacks)
    for _ in range(len(rucksacks) // 3):
        group = islice(it, 0, 3)
        c = Counter()
        for rucksack in group:
            c.update(set(rucksack))
        [(item, _)] = c.most_common(1)
        priority_sum += scores.get(item)
    return priority_sum


if __name__ == "__main__":
    test = dedent("""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""").splitlines()

    print(f"{part1() = }, {part2()}")