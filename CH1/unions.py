#!/usr/bin/env python
"""
Usage: script [-a AMT ]

Options:
    -h --help           Show this help.
    -v --version        Show the version.
    -a --amount AMT     The amount of barley.
"""
from docopt import docopt
from ctypes import *

class barley_amount(Union):
    _fields_ = [
            ("barley_long", c_long),
            ("barley_int", c_int),
            ("barley_char", c_char * 8),
            ]

def main(args):
    print args
    if args["--amount"]:
        my_barley = barley_amount(int(args["--amount"]))
    else:
        value = raw_input("Enter the amount of barley"
                "to put into the beer vat:")
        my_barley = barley_amount(int(value))
    print "Barley amount as long: %ld"  %(my_barley.barley_long)
    print "Barley amount as int: %d"    %(my_barley.barley_int)
    print "Barley amount as char: %s"   %(my_barley.barley_char)

if __name__ == '__main__':
    args = docopt(__doc__, version="Script 1.0")
    main(args)

