#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print(f"{len(sys.argv) - 1} arguments:")
if len(sys.argv) == 2:
    print(f"{len(sys.argv) - 1} argument:")
    print(f"{len(sys.argv) - 1}: {sys.argv[1]}")
if len(sys.argv) > 2:
    print(f"{len(sys.argv) - 1} arguments:")
    for i in range(len(sys.argv) - 1):
        print(f"{i + 1}: {sys.argv[i + 1]}")
