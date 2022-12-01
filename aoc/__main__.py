import aoc
import importlib
from pathlib import Path

def _get_and_call_else(obj: object, name: str, default: str) -> str:
    func = getattr(obj, name, None)
    return callable(func) and str(func()) or default

NOT_DONE_MESSAGE = "Not done!"

if __name__ == "__main__":
    print("=" * 20, "Advent of Code!", "=" * 20)
    root, *_ = aoc.__path__
    for child in sorted(Path(root).glob("day*.py"), key=lambda path: path.stem):
        module_path = ".".join(("aoc", child.stem))
        module = importlib.__import__(module_path, fromlist=["part1", "part2"])
        part1 = _get_and_call_else(module, "part1", NOT_DONE_MESSAGE)
        part2 = _get_and_call_else(module, "part2", NOT_DONE_MESSAGE)
        print(f"{child.stem:<5} => part1: {part1:<15} || part2: {part2}")
        
