#!/usr/bin/env python
import sys
import subprocess
import getpass


def print_usage():
    print("COMMAND: psme - Lists all processes running as the current user")
    print("USAGE: psme")


if len(sys.argv) != 1:
    print_usage()
    exit(1)
else:
    current_user = getpass.getuser()
    subprocess.call("ps -aux | grep %s" % current_user, shell=True)

