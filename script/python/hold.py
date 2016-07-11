#!/usr/bin/env python
import sys
import subprocess
import os.path


def print_usage():
    print("COMMAND: hold - attempts to create a file and 'tail -f' it to prevent automated logoff")
    print("USAGE: hold")


if len(sys.argv) != 1:
    print_usage()
    sys.exit(0)
else:
    with open(os.path.expanduser("~/.hold"), 'w+') as f:
        f.write("hold")
    subprocess.call("tail -f ~/.hold", shell=True)
