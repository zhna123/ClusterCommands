#!/usr/bin/env python
import sys
import subprocess
import getpass


def print_usage():
    print("COMMAND: copyfromlocal - attempts to copy a file from the local filesystem into your home directory on HDFS")
    print("USAGE: copyfromlocal <local file>")


if len(sys.argv) != 2:
    print_usage()
    sys.exit(0)
else:
    subprocess.Popen(['hadoop', 'fs', '-copyFromLocal', '%s' % sys.argv[1], 'hdfs:///user/%s/' % getpass.getuser()])
