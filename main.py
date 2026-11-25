import os
from pathlib import Path

# Returns RAW bytes
def get_dir_size(path: Path, files: list[tuple[Path, int]]) -> int:
    # base case is when path is a file, then get the size and return it
    if path.is_file():
        file_size = path.stat().st_size
        files.append((path, file_size))
        return file_size

    size = 0
    # recursive calls, 
    for f in path.iterdir():
        # for each path object, make recursive call
        size += get_dir_size(f, files)
    return size

# Made this function even tho it only does one call because in future will do more than just sort, maybewww
def sort_files_by_size(files: list[tuple[Path, int]]) -> list[tuple[Path, int]]:
    # sort based on file size - index 1
    sorted_list = sorted(files, reverse=True, key=lambda f: f[1])
    return sorted_list


# displays each file and shows percentage
def display_usage(sorted_files: list[tuple[Path, int]], total_fize_size: int) -> None:
    print(f"{'File':^75}{'Size':^12}{'Usage':^7}")
    
    for f in sorted_files:
        file_path = f[0]
        file_size = f[1]
        percentage_usage = (file_size / total_fize_size)  * 100
        unit_measurement = ''

        # if bigger than 1 gig, then just display in gig, else in mib, etc
        if file_size >= 2**30:
            file_size /= 2**30
            unit_measurement = 'GiB'
        elif file_size >= 1048576:
            file_size /= 2**20
            unit_measurement = 'MiB'
        else:   
            unit_measurement = 'bytes'

        print(f"{file_path.name:^75}{f'{file_size:.2f} {unit_measurement}':^12}{f'{percentage_usage:.2f}%':^7}")

if __name__ == '__main__':
    print("-----------Simple Disk Analyzer-----------\n")

    dir = input("Enter directory to check size: ")
    folder = Path.home() / dir

    if not folder.is_dir():
        print(f"folder does not exist or is a file")
        exit()

    files = []
    dir_size = get_dir_size(folder, files)
    dir_mb = dir_size * 10**-6
    dir_gb = dir_size * 10**-9
    print(F"bytes: {dir_size} bytes")
    print(f"dir size: {dir_mb:.2f}MB")
    print(f"dir size: {dir_gb:.2f}GB") 

    sorted_files = sort_files_by_size(files)
    display_usage(sorted_files, dir_size)

