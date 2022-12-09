from collections import defaultdict
import itertools
from pathlib import Path
import os

def load_data() -> str:
    return Path("./data/day7.txt").read_text()

def part1(it=None):
    sizes = defaultdict(int)
    if it is None:
        it = iter(load_data().splitlines())
    seen = set()
    ls_counts = defaultdict(int)
    while True:
        line = next(it, None)
        if line == None:
            break
        if line.startswith("$ cd"):
            if line == "$ cd /":
                pwd = ["/"]
            elif line.endswith(".."):
                pwd = pwd[:-1]
            else:
                pwd.append("".join(line[len("$ cd "):]))
        if line.startswith("$ ls"):
            items = []
            folder_path = "/" + "/".join(pwd[1:])
            line = next(it, None)
            while not (line is None or line.startswith("$")):
                items.append(line)
                # print(line)
                line = next(it, None)
            for item in items:
                if item.startswith("dir "):
                    continue
                size, name = item.split(" ")
                fname = folder_path + "/" + name 
                if fname in seen:
                    print("Already did ", fname)
                    continue
                else:
                    seen.add(fname)
                    sizes["/"] += int(size)
                    children = []
                    for child in pwd[1:]:
                        children.append(child)
                        path = "/" + "/".join(children)
                        # print(path)
                        sizes[path] += int(size)
            it = itertools.chain([line], it)
    total = 0
    for directory, size in sizes.items():
        if size <= 100000:
            total += size
    return total

def part2(it=None):
    required = 30000000
    capacity = 70000000
    sizes = defaultdict(int)
    if it is None:
        it = iter(load_data().splitlines())
    seen = set()
    while True:
        line = next(it, None)
        if line == None:
            break
        if line.startswith("$ cd"):
            if line == "$ cd /":
                pwd = ["/"]
            elif line.endswith(".."):
                pwd = pwd[:-1]
            else:
                pwd.append("".join(line[len("$ cd "):]))
        if line.startswith("$ ls"):
            items = []
            folder_path = "/" + "/".join(pwd[1:])
            line = next(it, None)
            while not (line is None or line.startswith("$")):
                items.append(line)
                # print(line)
                line = next(it, None)
            for item in items:
                if item.startswith("dir "):
                    continue
                size, name = item.split(" ")
                fname = folder_path + "/" + name 
                if fname in seen:
                    continue
                else:
                    seen.add(fname)
                    sizes["/"] += int(size)
                    children = []
                    for child in pwd[1:]:
                        children.append(child)
                        path = "/" + "/".join(children)
                        # print(path)
                        sizes[path] += int(size)
            it = itertools.chain([line], it)

    # print(sizes)
    to_free = required - (capacity - sizes["/"])
    size_amounts = [size for size in sizes.values() if size > to_free]
    # print(f"{min(size_amounts) = }")
    return min(size_amounts)
if __name__ == "__main__":
    test = iter("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines())
    
    print(f"{part1() = }")
    print(f"{part2() = }")