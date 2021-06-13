# Test of a function
import sys
import os

path = sys.argv[1]

if len(sys.argv) > 3:
    sys.exit(1)

leng = len(os.listdir(path))
print(leng)
