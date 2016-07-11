#!/usr/bin/env python
import sys
import subprocess
import getpass


def print_usage():
    print("COMMAND: copytolocal - attempts to copy a file from your home folder on HDFS to the local filesystem")
    print("USAGE: copytolocal <name of file which is in your home folder on HDFS>")

if len(sys.argv) != 2:
    print_usage()
    sys.exit(0)
else:
    subprocess.Popen(['hadoop', 'fs', '-copyToLocal', 'hdfs:///user/%s/%s' % (getpass.getuser(), sys.argv[1])])
