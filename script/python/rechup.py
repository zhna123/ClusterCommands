#!/usr/bin/env python
import sys
import subprocess


def print_usage():
    print("COMMAND: rechup - Runs a jar with hadoop and a bunch of extra options. Output is directed to file.")
    print("USAGE: rechup <jar name> \"<command and parameters in quotes>\" <output file name>")


if len(sys.argv) != 4:
    print_usage()
    exit(1)
else:
    current_directory = subprocess.Popen(['pwd'])
    subprocess.Popen(['export', "HADOOP_CLIENT_OPTS='-XX:MaxPermSize=512m -Xmx12288m -Dhttps.protocols=TLSv1'"], shell=True)
    subprocess.Popen(['export', "HADOOP_CLASSPATH=%s/%s" % (current_directory, sys.argv[1])], shell=True)
    childOpts = "-Xmx8000m -Xms1536M -Xss1M -XX:MaxPermSize=700M"
    # The first argument in childOpts needs to be ~2gb less than mapred.job.map.memory.mb and mapred.job.reduce.memory.mb
    subprocess.Popen(['nohup', 'hadoop', 'jar', '%s' % sys.argv[1], '-D mapred.child.java.opts = %s' % childOpts,
                      '-D mapred.map.java.opts = %s' % childOpts,
                      '-D mapred.reduce.java.opts = %s' % childOpts,
                      '-D mapred.job.map.memory.mb = 1000',
                      '-D mapred.job.reduce.memory.mb = 10000',
                      '-D hbase.rpc.timeout = 1000000',
                      '-D hbase.regionserver.lease.period = 1000000',
                      '-D mapred.task.timeout = 1800000',
                      '%s' % sys.argv[2],
                      '2> %s' % sys.argv[3],
                      '1> %s' % sys.argv[3],
                      '&'], shell=True)



