#!/usr/bin/env python
import sys
import subprocess


def print_usage():
    print("COMMAND: cconf - appends something content-record config.yaml's table names")
    print("USAGE: cconf <target config file> <optional replacement text>")

if len(sys.argv) < 1:
    print_usage()
    sys.exit(0)
else:
    file_name = sys.argv[1]
    if len(sys.argv) > 2:
        append_text = sys.argv[2]
    else:
        append_text = "MAC"

subprocess.Popen(['sed', '-i', 's/refrecord_nomenclature_v2/%s_refrecord_nomenclature_v2/g' % append_text, '%s' % file_name])
subprocess.Popen(['sed', '-i', 's/refrecord_content_meta_v2/%s_refrecord_content_meta_v2/g' % append_text, '%s' % file_name])
subprocess.Popen(['sed', '-i', 's/refrecord_content_npi_v2/%s_refrecord_content_npi_v2/g' % append_text, '%s' % file_name])

# OR using python file operation to do the in-place replace
# with open(file_name, 'r+') as f:
#     content = f.read()
#     f.seek(0)
#     f.truncate()
#     content = content.replace("refrecord_nomenclature_v2", "%s_refrecord_nomenclature_v2" % append_text)
#     content = content.replace("refrecord_content_meta_v2", "%s_refrecord_content_meta_v2" % append_text)
#     content = content.replace("refrecord_content_npi_v2", "%s_refrecord_content_npi_v2" % append_text)
#     f.write(content)
