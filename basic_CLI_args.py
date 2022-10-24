#! /usr/bin/env python

import sys

args = sys.argv
lenofargs = len(args)
lastindex = lenofargs-1

print(f"HERE ARE MY ARGUMENTS: {args}")
print(f"This is the first argument: {args[1]}")
print(f"These are the useful args: {args[1:lenofargs]}")
