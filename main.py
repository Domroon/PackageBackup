import subprocess
from pathlib import Path


def main():
    path = Path() / 'packagesTextfile'
    packages_file = open(path / "packages.txt")
    lines = packages_file.readlines()
    package_names = []
    for line in lines:
        package_names.append(line.split(' ')[0])

    subprocess.run(["yay", "--noconfirm"])
    for package in package_names:
        subprocess.run(["yay", "-S", "--noconfirm", package])


if __name__ == '__main__':
    main()