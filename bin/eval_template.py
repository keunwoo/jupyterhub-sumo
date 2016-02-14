#!/usr/bin/env python

import json
import sys


def usage():
    print ('''
USAGE: %(cmdname)s jsonpath templatepath outpath

	jsonpath is a path to a file containing a JSON object
		describing the substitution map.
	templatefile is the path to the input template.
	outpath is the path to the output file.
    '''.rstrip(' ') % {
        'cmdname': sys.argv[0],
    })


def main(argv):
    if len(argv) != 4:
        usage()
        sys.exit(1)

    jsonpath = argv[1]
    templatepath = argv[2]
    outpath = argv[3]

    with open(templatepath) as f:
        template = f.read()

    with open(jsonpath) as f:
        j = json.load(f)

    out = template
    for k, v in j.items():
        out = out.replace(k, v)

    with open(outpath, 'wb') as f:
        f.write(out)


if __name__ == '__main__':
    main(sys.argv)
