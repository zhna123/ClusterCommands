#!/usr/bin/env python
import sys
import subprocess


def print_usage():
    print("COMMAND: runjar - Runs a jar with hadoop and a bunch of extra options.")
    print("USAGE: runjar <jar name> <whatever else, but don't use quotes>")


if len(sys.argv) < 2:
    print_usage()
    exit(1)
else:
    current_directory = subprocess.Popen(['pwd'])
    jar_name = sys.argv[1]
    subprocess.Popen(['shift'], shell=True)
    subprocess.Popen(['export', "HADOOP_CLIENT_OPTS='-XX:MaxPermSize=512m -Xmx12288m'"], shell=True)
    # -Dhttps.protocols=TLSv1
    subprocess.Popen('export', 'HADOOP_CLASSPATH=%s/%s' % (current_directory, jar_name))
    childOpts = "-Xmx6144m -Xms1536M -Xss1M -XX:MaxPermSize=700M"
    # The first argument in childOpts needs to be ~2gb less than mapred.job.map.memory.mb and mapred.job.reduce.memory.mb
    subprocess.Popen(['hadoop', 'jar', '%s' % jar_name, '-D mapred.child.java.opts = %s' % childOpts,
                      '-D mapred.map.java.opts = %s' % childOpts,
                      '-D mapred.reduce.java.opts = %s' % childOpts,
                      '-D mapred.job.map.memory.mb = 1000',
                      '-D mapred.job.reduce.memory.mb = 10000',
                      '-D hbase.rpc.timeout = 1000000',
                      '-D hbase.regionserver.lease.period = 1000000',
                      '-D mapred.task.timeout = 1800000',
                      '$@'], shell=True)

