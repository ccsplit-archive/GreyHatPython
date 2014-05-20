#!/usr/bin/env python
from ctypes import *

msvcrt = cdll.LoadLibrary("libc.so.6")
message_string = "Hello world!\n"
msvcrt.printf("Testing: %s", message_string)
