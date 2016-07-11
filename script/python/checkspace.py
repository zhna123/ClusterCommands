#!/usr/bin/env python
# we can name the script using .sh extension with above line added.
import sys
import subprocess


def print_usage():
    print("COMMAND: checkspace - Lists the folders in the current directory and how big they are")
    print("USAGE: checkspace")

# first argument is the name of the script being run
if len(sys.argv) != 1:
    print_usage()
    sys.exit(0)
else:
    print("FILESYSTEM STATS:")
    subprocess.call("df -h", shell=True)
    print("CURRENT DIRECTORY STATS:")
    subprocess.call("sudo du -smc * | sort -n", shell=True)

