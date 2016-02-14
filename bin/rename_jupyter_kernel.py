#!/usr/bin/env python

import json
import sys


def usage():
    print ('''
USAGE: %(cmdname)s kernel.json displayname

	where kernel.json is path to the kernel json, and displayname is
	the new diplayname.

	Output is written back to original file.
    '''.rstrip(' ') % {
        'cmdname': sys.argv[0],
    })


def main(argv):
    if len(argv) != 3:
        usage()
        sys.exit(1)

    kernel_file = argv[1]
    display_name = argv[2]

    with open(kernel_file, 'r') as f:
        parsed = json.load(f)

    parsed['display_name'] = display_name
    updated = json.dumps(parsed, indent=4)

    with open(kernel_file, 'w') as f:
        f.write(updated)


if __name__ == '__main__':
    main(sys.argv)
