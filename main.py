import os
from pathlib import Path


# Returns RAW bytes
def get_dir_size(path: Path) -> int:
    # base case is when path is a file, then get the size and return it
    if path.is_file():
        print("recursive case made")
        print(path)
        return path.stat().st_size

    size = 0
    # recursive calls, 
    breakpoint
    for f in path.iterdir():
        # for each path object, make recursive call
        size += get_dir_size(f)
    return size



if __name__ == '__main__':
    print("--------Simple Disk Analyzer--------\n")

    dir = input("Enter directory to check size: ")
    folder = Path.home() / dir

    if not folder.is_dir():
        print(f"folder does not exist or is a file")

    dir_size = get_dir_size(folder)
    dir_mb = dir_size // 2**20
    dir_gb = dir_mb // 1024
    print(f"dir size: {dir_mb}mb")
    print(f"dir size: {dir_gb}gb")

