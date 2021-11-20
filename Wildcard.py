# nama file: Wildcard.py
import fnmatch

key = input()
length = int(input())
solve = []

for i in range(length):
    value = input()
    if fnmatch.fnmatch(value, key):
        solve.append(value)

for i in range(len(solve)):
    print(solve[i])
