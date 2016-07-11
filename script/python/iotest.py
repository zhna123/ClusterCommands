import os.path
import sys


print("start testing...")
directory = "/Users/nz026920/python_cog/test/"
fpath = os.path.join(directory, "Alert.avdl")
with open(fpath, 'r') as f:
    for line in f:
        word_list = line.split()
        if len(word_list) == 0:
            continue
        if word_list[0] == "record":
            print(word_list[1])

