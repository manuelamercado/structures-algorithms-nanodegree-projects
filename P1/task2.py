"""
Finding Files
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path) https://docs.python.org/3.7/library/os.path.html#os.path.isdir

os.path.isfile(path) https://docs.python.org/3.7/library/os.path.html#os.path.isfile

os.listdir(directory) https://docs.python.org/3.7/library/os.html#os.listdir

os.path.join(...) https://docs.python.org/3.7/library/os.path.html#os.path.join

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

Here is some code for the function to get you started:
"""
from genericpath import isfile
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    result = []

    for file in os.listdir(path):
        current_path = os.path.join(path, file)

        if os.path.isfile(current_path) and current_path.endswith(suffix):
            result.append(current_path)
        elif os.path.isdir(current_path):
            result.extend(find_files(suffix, current_path))

    return result


result = find_files('.c', './testdir')
print('.c files ---->')
for file in result:
    print(file)
# './testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c'
result = find_files('.h', './testdir')
print('.h files ---->')
for file in result:
    print(file)
# './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h'
result = find_files('.x', './testdir')
print('.x files ---->')
for file in result:
    print(file)
# []
