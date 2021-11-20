# nama file : Pasar_Rakyat.py
import math

N = int(input())
val = [0 for i in range(N)]

for i in range(N):
    val[i] = int(input())

x = 1
for i in val:
    x = x * i // math.gcd(x, i)
print(x)