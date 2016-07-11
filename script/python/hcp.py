#!/usr/bin/env python
import sys
import subprocess


def print_usage():
    print("COMMAND: . hcp - Adds a jar in the current folder to the hadoop classpath.")
    print("USAGE: . hcp <jar name>")
    print("NOTE: This command MUST be run with a \".\" preceding it. Otherwise, it will seem to have no effect.")

if len(sys.argv) < 2:
    print_usage()
    sys.exit(0)
else:
    print("NOTE: This command MUST be run with a \".\" preceding it. Otherwise, it will seem to have no effect.")
    current_directory = subprocess.Popen(['pwd'])
    current_hadoop_classpath = subprocess.Popen(['echo', '$HADOOP_CLASSPATH'])
    print("previous classpath: %s" % current_hadoop_classpath)
    subprocess.Popen(['export', 'HADOOP_CLASSPATH=%s:%s/%s' % (current_hadoop_classpath, current_directory, sys.argv[1])])
    new_classpath = subprocess.Popen(['echo', '$HADOOP_CLASSPATH'])
    print("current classpath: %s" % new_classpath)