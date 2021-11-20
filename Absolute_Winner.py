# nama file : Absolute_Winner.py

x, y, z = map(int, input().split())

total = 4 * (x + y + z) / 7
if x == total or y == total or z == total:
    print("YA")
else:
    print("TIDAK")
