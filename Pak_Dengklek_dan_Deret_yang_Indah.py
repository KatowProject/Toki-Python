# nama file: Pak_Dengklek_dan_Deret_yang_Indah.py

val, length, res = map(int, input().split(" "))

i = 0
while i < length:
    print(val)
    val = val + res
    i += 1
